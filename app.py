import os
import logging
from datetime import datetime
from flask import Flask, jsonify, render_template, request
from google.cloud import bigquery
from google.oauth2 import service_account
from dotenv import load_dotenv

# Configurar logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Cargar variables de entorno si existe un archivo .env
load_dotenv()

app = Flask(__name__)

# Configuración de BigQuery
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT", "project-c0f821cf-8af2-411b-811")
DATASET_ID = os.getenv("BIGQUERY_DATASET", "Proyecto_IOT")
TABLE_ID = os.getenv("BIGQUERY_TABLE", "control_inventarios")
TABLE_FULL_NAME = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

def get_bigquery_client():
    """
    Intenta inicializar el cliente de BigQuery de manera robusta.
    1. Si GOOGLE_APPLICATION_CREDENTIALS está definida y el archivo existe, lo usa.
    2. De lo contrario, intenta usar Application Default Credentials (ADC).
    """
    creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    
    try:
        if creds_path and os.path.exists(creds_path):
            logging.info(f"Conectando a BigQuery usando cuenta de servicio en: {creds_path}")
            credentials = service_account.Credentials.from_service_account_file(creds_path)
            return bigquery.Client(credentials=credentials, project=PROJECT_ID)
        else:
            logging.info("GOOGLE_APPLICATION_CREDENTIALS no definida o archivo no encontrado. Intentando usar Application Default Credentials (ADC)...")
            return bigquery.Client(project=PROJECT_ID)
    except Exception as e:
        logging.error(f"Error al inicializar el cliente de BigQuery: {e}")
        return None

# Inicializar cliente de BigQuery al arrancar
bq_client = get_bigquery_client()

@app.route("/")
def index():
    """Sirve la página web principal del Dashboard."""
    return render_template("index.html")

@app.route("/api/status", methods=["GET"])
def connection_status():
    """Devuelve el estado de la conexión a BigQuery y detalles de configuración."""
    global bq_client
    if not bq_client:
        bq_client = get_bigquery_client()
        
    if bq_client:
        try:
            # Probar la conexión haciendo una consulta simple de lista de tablas
            bq_client.list_tables(f"{PROJECT_ID}.{DATASET_ID}", max_results=1)
            return jsonify({
                "status": "connected",
                "message": "Conectado exitosamente a BigQuery",
                "config": {
                    "project_id": PROJECT_ID,
                    "dataset_id": DATASET_ID,
                    "table_id": TABLE_ID,
                    "table_full_name": TABLE_FULL_NAME
                }
            })
        except Exception as e:
            return jsonify({
                "status": "error",
                "message": f"Cliente inicializado pero falló la prueba de conexión: {str(e)}",
                "config": {
                    "project_id": PROJECT_ID,
                    "dataset_id": DATASET_ID,
                    "table_id": TABLE_ID,
                    "table_full_name": TABLE_FULL_NAME
                }
            }), 200
    else:
        return jsonify({
            "status": "disconnected",
            "message": "No se pudo conectar a BigQuery. Verifica tus credenciales (archivo JSON o variables de entorno).",
            "config": {
                "project_id": PROJECT_ID,
                "dataset_id": DATASET_ID,
                "table_id": TABLE_ID,
                "table_full_name": TABLE_FULL_NAME
            }
        }), 200

@app.route("/api/data", methods=["GET"])
def get_data():
    """Obtiene datos de la tabla de BigQuery con opciones de búsqueda, filtro y ordenamiento."""
    global bq_client
    if not bq_client:
        return jsonify({"error": "BigQuery no está conectado"}), 500
        
    search = request.args.get("search", "")
    familia = request.args.get("familia", "")
    limit = request.args.get("limit", 100, type=int)
    
    query = f"SELECT * FROM `{TABLE_FULL_NAME}`"
    conditions = []
    
    if search:
        # Búsqueda parcial segura en campos de texto (escapar comillas simples para evitar inyección)
        search_escaped = search.replace("'", "''")
        conditions.append(f"(LOWER(item_material) LIKE LOWER('%{search_escaped}%') OR LOWER(nro_vale) LIKE LOWER('%{search_escaped}%'))")
    if familia:
        familia_escaped = familia.replace("'", "''")
        conditions.append(f"LOWER(familia_material) = LOWER('{familia_escaped}')")
        
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
        
    query += " ORDER BY fecha_registro DESC, nro_vale DESC"
    query += f" LIMIT {limit}"
    
    try:
        logging.info(f"Ejecutando consulta en BigQuery: {query}")
        query_job = bq_client.query(query)
        results = query_job.result()
        
        data = []
        for row in results:
            row_dict = dict(row.items())
            if row_dict.get("fecha_registro"):
                row_dict["fecha_registro"] = str(row_dict["fecha_registro"])
            data.append(row_dict)
            
        return jsonify(data)
    except Exception as e:
        logging.error(f"Error al ejecutar consulta: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/api/stats", methods=["GET"])
def get_stats():
    """
    Obtiene estadísticas generales avanzadas y agregados analíticos para el Dashboard.
    Actúa como un motor de Business Intelligence (BI) especializado en logística de construcción.
    """
    global bq_client
    if not bq_client:
        return jsonify({"error": "BigQuery no está conectado"}), 500
        
    try:
        # 1. KPIs Generales (Métricas de Negocio de Alto Valor)
        # - total_transacciones: Volumen de actividad logística.
        # - stock_total: Unidades totales inmovilizadas en almacén/obra.
        # - nivel_servicio: Porcentaje de ítems que cumplen con el inventario de seguridad.
        # - alertas_stock: Cantidad de ítems en riesgo inminente de quiebre (Stockout).
        # - frentes_activos: Cantidad de proyectos de obra civil que están consumiendo materiales.
        query_kpis = f"""
        SELECT 
            COUNT(*) as total_transacciones,
            COALESCE(SUM(existencia_actual), 0) as stock_total,
            ROUND(SAFE_DIVIDE(COUNTIF(existencia_actual >= inventario_seguridad), COUNT(*)) * 100, 1) as nivel_servicio,
            COUNTIF(existencia_actual < inventario_seguridad) as alertas_stock,
            COUNT(DISTINCT frente_o_bodega) as frentes_activos
        FROM `{TABLE_FULL_NAME}`
        """
        job_kpis = bq_client.query(query_kpis)
        kpis_res = list(job_kpis.result())[0]
        
        # 2. Salud del Inventario (Riesgo de Quiebre de Stock)
        # Clasifica el inventario según el nivel de riesgo de detener la obra civil.
        query_salud = f"""
        SELECT 
            CASE 
                WHEN existencia_actual = 0 THEN 'Crítico (Agotado)'
                WHEN existencia_actual < inventario_seguridad THEN 'Riesgo (Bajo Mínimo)'
                ELSE 'Saludable (Óptimo)'
            END as estado_salud,
            COUNT(*) as cantidad
        FROM `{TABLE_FULL_NAME}`
        GROUP BY estado_salud
        ORDER BY cantidad DESC
        """
        job_salud = bq_client.query(query_salud)
        salud = [{"estado": row["estado_salud"], "cantidad": row["cantidad"]} for row in job_salud.result()]
        
        # 3. Distribución por Frente de Obra / Proyecto
        # Identifica qué proyectos de construcción o bodegas concentran la mayor cantidad de recursos.
        query_frentes = f"""
        SELECT 
            COALESCE(frente_o_bodega, 'Sin Asignar') as frente,
            COALESCE(SUM(existencia_actual), 0) as stock
        FROM `{TABLE_FULL_NAME}`
        GROUP BY frente
        ORDER BY stock DESC
        LIMIT 5
        """
        job_frentes = bq_client.query(query_frentes)
        frentes = [{"frente": row["frente"], "stock": row["stock"]} for row in job_frentes.result()]
        
        # 4. Análisis de Prioridad y Brecha (Gap Analysis)
        # Muestra el nivel promedio de inventario real frente al nivel de seguridad por prioridad.
        # Esto permite ver si se están descuidando los materiales de prioridad "ALTA".
        query_prioridad = f"""
        SELECT 
            COALESCE(prioridad_abastecimiento, 'MEDIA') as prioridad,
            ROUND(AVG(existencia_actual), 1) as avg_actual,
            ROUND(AVG(inventario_seguridad), 1) as avg_seguridad
        FROM `{TABLE_FULL_NAME}`
        GROUP BY prioridad
        ORDER BY 
            CASE prioridad 
                WHEN 'ALTA' THEN 1 
                WHEN 'MEDIA' THEN 2 
                ELSE 3 
            END
        """
        job_prioridad = bq_client.query(query_prioridad)
        prioridades = [{
            "prioridad": row["prioridad"], 
            "avg_actual": float(row["avg_actual"]), 
            "avg_seguridad": float(row["avg_seguridad"])
        } for row in job_prioridad.result()]
        
        # 5. Análisis del Flujo Logístico (Entradas vs. Salidas)
        # Muestra la relación entre abastecimientos (entradas) y consumos en frente de obra (salidas).
        query_flujo = f"""
        SELECT 
            COALESCE(flujo_almacen, 'NO ESPECIFICADO') as flujo,
            COUNT(*) as transacciones,
            COALESCE(SUM(ABS(cantidad_transaccion)), 0) as volumen_total
        FROM `{TABLE_FULL_NAME}`
        GROUP BY flujo
        ORDER BY transacciones DESC
        """
        job_flujo = bq_client.query(query_flujo)
        flujo = [{"flujo": row["flujo"], "transacciones": row["transacciones"], "volumen": row["volumen_total"]} for row in job_flujo.result()]
        
        # 6. Top 5 de Materiales por Stock en Almacén
        query_familias = f"""
        SELECT 
            COALESCE(familia_material, 'Sin Familia') as familia,
            COALESCE(SUM(existencia_actual), 0) as stock
        FROM `{TABLE_FULL_NAME}`
        GROUP BY familia
        ORDER BY stock DESC
        LIMIT 5
        """
        job_familias = bq_client.query(query_familias)
        familias = [{"familia": row["familia"], "stock": row["stock"]} for row in job_familias.result()]
        
        return jsonify({
            "kpis": {
                "total_transacciones": kpis_res["total_transacciones"],
                "stock_total": kpis_res["stock_total"],
                "nivel_servicio": kpis_res["nivel_servicio"] if kpis_res["nivel_servicio"] is not None else 100.0,
                "alertas_stock": kpis_res["alertas_stock"],
                "frentes_activos": kpis_res["frentes_activos"]
            },
            "salud": salud,
            "frentes": frentes,
            "prioridades": prioridades,
            "flujo": flujo,
            "familias": familias
        })
    except Exception as e:
        logging.error(f"Error al calcular estadísticas avanzadas de BI: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/api/data", methods=["POST"])
def add_data():
    """Registra un nuevo movimiento de inventario insertando una fila en la tabla de BigQuery."""
    global bq_client
    if not bq_client:
        return jsonify({"error": "BigQuery no está conectado"}), 500
        
    data = request.json
    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400
        
    # Validar campos obligatorios
    required_fields = ["nro_vale", "fecha_registro", "item_material", "existencia_actual"]
    for field in required_fields:
        if field not in data or data[field] == "":
            return jsonify({"error": f"El campo '{field}' es requerido"}), 400
            
    # Formatear y validar la fecha
    try:
        datetime.strptime(data["fecha_registro"], "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "Formato de fecha inválido. Utilice AAAA-MM-DD."}), 400
        
    # Escapar cadenas de texto simples para evitar inyección SQL
    def clean_str(val):
        return str(val).replace("'", "''") if val is not None else None

    # Construir fila a insertar respetando el esquema exacto de la base de datos
    row_to_insert = {
        "nro_vale": clean_str(data.get("nro_vale")),
        "fecha_registro": data.get("fecha_registro"),
        "item_material": clean_str(data.get("item_material")),
        "familia_material": clean_str(data.get("familia_material")),
        "flujo_almacen": clean_str(data.get("flujo_almacen")),
        "cantidad_transaccion": int(data.get("cantidad_transaccion")) if data.get("cantidad_transaccion") is not None else 0,
        "existencia_anterior": int(data.get("existencia_anterior")) if data.get("existencia_anterior") is not None else 0,
        "existencia_actual": int(data.get("existencia_actual")),
        "inventario_seguridad": int(data.get("inventario_seguridad")) if data.get("inventario_seguridad") is not None else 0,
        "estado_disponibilidad": clean_str(data.get("estado_disponibilidad")),
        "frente_o_bodega": clean_str(data.get("frente_o_bodega")),
        "unidad_control": clean_str(data.get("unidad_control")),
        "prioridad_abastecimiento": clean_str(data.get("prioridad_abastecimiento")),
        "concepto_logitico": clean_str(data.get("concepto_logitico"))
    }
    
    try:
        # 1. Intentar inserción en Streaming (rápido y estándar en SDK)
        table_ref = bq_client.dataset(DATASET_ID).table(TABLE_ID)
        logging.info(f"Intentando inserción por Streaming en BigQuery: {row_to_insert}")
        
        errors = bq_client.insert_rows_json(table_ref, [row_to_insert])
        
        if errors == []:
            return jsonify({"success": True, "message": "Registro de inventario guardado por Streaming."}), 201
        else:
            logging.warning(f"Fallo Streaming insert ({errors}). Intentando inserción DML de respaldo...")
            raise Exception("Streaming insert rejected rows.")
            
    except Exception as e:
        # 2. Respaldo DML (SQL INSERT) - Excelente para tablas recién creadas o con restricciones de cuota
        try:
            logging.info("Ejecutando inserción SQL DML de respaldo...")
            query = f"""
            INSERT INTO `{TABLE_FULL_NAME}` (
                nro_vale, fecha_registro, item_material, familia_material, flujo_almacen,
                cantidad_transaccion, existencia_anterior, existencia_actual, inventario_seguridad,
                estado_disponibilidad, frente_o_bodega, unidad_control, prioridad_abastecimiento, concepto_logitico
            ) VALUES (
                '{row_to_insert["nro_vale"]}', 
                DATE('{row_to_insert["fecha_registro"]}'), 
                '{row_to_insert["item_material"]}', 
                {'NULL' if not row_to_insert["familia_material"] else f"'{row_to_insert['familia_material']}'"}, 
                {'NULL' if not row_to_insert["flujo_almacen"] else f"'{row_to_insert['flujo_almacen']}'"}, 
                {row_to_insert["cantidad_transaccion"]}, 
                {row_to_insert["existencia_anterior"]}, 
                {row_to_insert["existencia_actual"]}, 
                {row_to_insert["inventario_seguridad"]}, 
                {'NULL' if not row_to_insert["estado_disponibilidad"] else f"'{row_to_insert['estado_disponibilidad']}'"}, 
                {'NULL' if not row_to_insert["frente_o_bodega"] else f"'{row_to_insert['frente_o_bodega']}'"}, 
                {'NULL' if not row_to_insert["unidad_control"] else f"'{row_to_insert['unidad_control']}'"}, 
                {'NULL' if not row_to_insert["prioridad_abastecimiento"] else f"'{row_to_insert['prioridad_abastecimiento']}'"}, 
                {'NULL' if not row_to_insert["concepto_logitico"] else f"'{row_to_insert['concepto_logitico']}'"}
            )
            """
            bq_client.query(query).result()
            return jsonify({"success": True, "message": "Registro de inventario guardado vía SQL DML."}), 201
        except Exception as dml_error:
            logging.error(f"Fallo inserción DML de respaldo: {dml_error}")
            return jsonify({
                "error": "No se pudo insertar el registro en BigQuery.",
                "details": str(dml_error)
            }), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    debug = os.getenv("FLASK_ENV") == "development"
    logging.info(f"Iniciando servidor Flask en puerto {port} (debug={debug})")
    app.run(host="0.0.0.0", port=port, debug=debug)
