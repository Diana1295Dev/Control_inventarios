# 🏗️ Dashboard Inteligente de Control de Inventarios para Constructoras

Este es un dashboard premium interactivo y en tiempo real diseñado específicamente para la logística, el control de abastecimiento y la prevención de quiebres de obra en empresas de construcción. La aplicación se conecta de forma nativa a **Google BigQuery** utilizando un backend robusto en Flask (Python) y una interfaz de usuario glassmórfica premium impulsada por **Chart.js** para visualización analítica avanzada.

---

## 📊 Propuesta de Valor y Métricas de Negocio (Business Intelligence)

En una empresa constructora, el desabastecimiento de materiales críticos (cemento, acero, tuberías, aditivos) puede paralizar frentes de obra enteros, ocasionando pérdidas financieras monumentales por retrasos de maquinaria y mano de obra. 

Este dashboard no es solo un registrador de transacciones; actúa como un **Asistente de Inteligencia de Negocios** que analiza en tiempo real:

1. **Nivel de Servicio de Obra (%)**: Porcentaje de materiales en stock que están garantizados por encima del inventario de seguridad. Mide la salud global de la cadena de suministro ante variaciones de demanda o demoras de proveedores.
2. **Salud del Inventario (Riesgo de Quiebre de Stock)**:
   * 🔴 **Stock Crítico (Quiebre de Obra)**: Existencia actual es `0` o menor (parada inminente).
   * 🟡 **Stock en Riesgo**: Existencia actual está por debajo del *Inventario de Seguridad* definido para ese material.
   * 🟢 **Disponible / Saludable**: Existencia actual supera cómodamente los límites críticos de seguridad.
3. **Brecha por Prioridad (Actual vs. Seguridad)**: Compara visualmente cuántas unidades de stock promedio se tienen en comparación con el stock mínimo de seguridad definido, desglosado por materiales de prioridad **Alta**, **Media** y **Baja**. Permite a los jefes de compras priorizar órdenes de compra de materiales tipo "A" (alta prioridad).
4. **Consumo por Frente de Trabajo o Proyecto**: Identifica qué obras civiles independientes están demandando mayor flujo de inventario, permitiendo realizar prorrateos de costos eficientes.
5. **Balance Logístico (Entradas vs. Salidas)**: Mide el volumen de materiales que ingresan a bodega contra los despachados a frentes de obra, ayudando a monitorear la velocidad de rotación de inventarios.

---

## 🛠️ Stack Tecnológico

* **Backend**: Flask (Python 3.11), SDK de Google Cloud BigQuery, Pandas (para modelado analítico).
* **Frontend**: HTML5, Vanilla CSS3 (estilo premium Glassmorphic optimizado para modo oscuro), JavaScript (ES6+), y **Chart.js** para visualización analítica interactiva de gráficos.
* **Infraestructura**: Contenedorizado con **Docker**, optimizado para ejecutarse en **Google Cloud Run** y escalar a cero.
* **Base de Datos**: **Google BigQuery** (almacenamiento analítico de alto rendimiento a escala de Petabytes).

---

## 📁 Esquema de Datos de BigQuery

La tabla analítica conectada en BigQuery debe tener los siguientes nombres de columna exactos:

| Nombre del Campo | Tipo de Dato | Descripción |
| :--- | :--- | :--- |
| `nro_vale` | `STRING` | Número de comprobante o vale de almacén. |
| `fecha_registro` | `DATE` | Fecha del movimiento de inventario. |
| `item_material` | `STRING` | Nombre, código o descripción detallada del material. |
| `familia_material` | `STRING` | Categoría logística (ej. Aceros, Tuberías, Agregados). |
| `flujo_almacen` | `STRING` | Tipo de movimiento: `ENTRADA` o `SALIDA`. |
| `cantidad_transaccion` | `INTEGER` | Cantidad de unidades transaccionadas (positivo o negativo). |
| `existencia_anterior` | `INTEGER` | Cantidad física en bodega antes del movimiento. |
| `existencia_actual` | `INTEGER` | Cantidad física final en bodega (Existencia Anterior + Cantidad Transacción). |
| `inventario_seguridad` | `INTEGER` | Stock mínimo de seguridad para el material. |
| `estado_disponibilidad` | `STRING` | Estado (DISPONIBLE, STOCK MINIMO, AGOTADO). |
| `frente_o_bodega` | `STRING` | Nombre del Frente de Obra civil o bodega de destino. |
| `unidad_control` | `STRING` | Unidad de medida (ej. UNIDAD, METROS, KG). |
| `prioridad_abastecimiento`| `STRING` | Criticidad del material para la obra (ALTA, MEDIA, BAJA). |
| `concepto_logitico` | `STRING` | Concepto del movimiento (*Respetar tipografía exacta sin la 's'*). |

---

## 🚀 Arquitectura de Ingestión Resiliente (Fallback Inteligente)

Para garantizar un 100% de éxito en la escritura de registros desde el panel táctil interactivo, el backend en `app.py` implementa un flujo híbrido robusto de inserción:
1. **Streaming Ingestion (`insert_rows_json`)**: Primero intenta insertar filas directamente en el búfer de streaming de BigQuery de manera síncrona.
2. **Fallback SQL DML (`INSERT INTO ... VALUES`)**: Si la API de streaming rechaza la transacción por retrasos de propagación o límites de cuota temporales (común en datasets recién creados), el sistema atrapa el error de forma segura y ejecuta una sentencia SQL DML de inserción a través de un Query Job tradicional.

---

## 💻 Configuración Local para Desarrollo

### 1. Requisitos Previos
* Python 3.9 o superior instalado.
* Una cuenta de Google Cloud con un proyecto activo y habilitada la API de BigQuery.
* Un archivo de credenciales de Service Account en formato JSON (`credentials.json`).

### 2. Pasos de Instalación
1. Clona el repositorio o accede a la carpeta del proyecto.
2. Crea un entorno virtual e instala las dependencias:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate   # En Windows
   source venv/bin/activate  # En Linux/macOS
   pip install -r requirements.txt
   ```
3. Copia el archivo `.env.example` a `.env`:
   ```bash
   cp .env.example .env
   ```
4. Configura las variables de entorno en el `.env` recién creado:
   ```env
   FLASK_ENV=development
   PORT=8080
   GOOGLE_APPLICATION_CREDENTIALS=ruta/a/tu/credentials.json
   GCP_PROJECT_ID=tu-proyecto-gcp
   BQ_DATASET_ID=Proyecto_IOT
   BQ_TABLE_ID=control_inventarios
   ```

### 3. Ejecutar la Aplicación Localmente
Inicia el servidor Flask de desarrollo:
```bash
python app.py
```
Abre en tu navegador la URL: `http://localhost:8080`

---

## 🐋 Despliegue en Producción (Google Cloud Run)

La aplicación está completamente dockerizada y lista para Cloud Run, aprovechando las ventajas de servidor sin estado y escalabilidad automática rápida.

### Paso 1: Compilar la Imagen Docker en local (Opcional para pruebas)
```bash
docker build -t control-inventarios-app .
docker run -p 8080:8080 --env-file .env control-inventarios-app
```

### Paso 2: Despliegue Automatizado con Google Cloud SDK
Ejecuta la siguiente suite de comandos para construir la imagen en la nube con **Cloud Build** y desplegarla en **Cloud Run**:

1. **Configurar el proyecto en el CLI**:
   ```bash
   gcloud config set project tu-proyecto-gcp
   ```

2. **Compilar la imagen en Google Artifact Registry**:
   ```bash
   gcloud builds submit --tag gcr.io/tu-proyecto-gcp/control-inventarios:latest
   ```

3. **Desplegar el servicio en Cloud Run**:
   ```bash
   gcloud run deploy control-inventarios \
     --image gcr.io/tu-proyecto-gcp/control-inventarios:latest \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --set-env-vars GCP_PROJECT_ID=tu-proyecto-gcp,BQ_DATASET_ID=Proyecto_IOT,BQ_TABLE_ID=control_inventarios
   ```

> [!IMPORTANT]
> **Permisos de Identidad en GCP**: Al desplegar en Cloud Run, no necesitas adjuntar un archivo JSON de credenciales. Cloud Run utiliza automáticamente la **Service Account por defecto** de tu servicio de Cloud Run. Asegúrate de concederle a dicha Service Account el rol de **Administrador de Datos de BigQuery** (`roles/bigquery.dataOwner`) o **Usuario de BigQuery** (`roles/bigquery.user`) en el panel de IAM de Google Cloud Console.

---

## ⚡ Autores y Soporte
Este panel fue estructurado e implementado con pasión y excelencia técnica por un **Experto en Business Intelligence & Cloud Software Architecture**. Para soporte o mejoras analíticas adicionales, contáctanos. 🏗️📈
