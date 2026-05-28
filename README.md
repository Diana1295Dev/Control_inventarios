# 🏗️ Dashboard Inteligente de Control de Inventarios para Constructoras

Este es un dashboard premium interactivo y en tiempo real diseñado específicamente para la analítica de datos logísticos, control de abastecimiento y prevención de quiebres de obra en empresas de construcción mediante ingesta de datos en tiempo real. La aplicación se conecta de forma nativa a **Google BigQuery** utilizando un backend robusto en Flask (Python) y una interfaz de usuario glassmórfica premium impulsada por **Chart.js** para visualización analítica avanzada.

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

## 📈 ¿Cómo interpretar nuestros gráficos? Guía práctica para la toma de decisiones

Diseñamos estas 4 visualizaciones para que no sean simples dibujos estáticos con números abstractos. Queremos que cada gráfico sea como un compañero de equipo que te cuenta qué está pasando en la obra en tiempo real y te ayuda a tomar decisiones rápidas para evitar que los proyectos se detengan.

Aquí te explicamos de manera muy sencilla y humana cómo leer cada uno de ellos:

---

### 1. Gráfico de Salud del Inventario (Dona)
*   **¿Qué nos muestra al primer vistazo?**
    Es como tomarle la temperatura a nuestro almacén. Nos divide todos los materiales en tres colores muy intuitivos:
    *   🔴 **Crítico (Agotado)**: Materiales que se nos terminaron por completo (¡alerta roja, la obra se puede parar!).
    *   🟡 **Riesgo (Bajo Mínimo)**: Insumos que todavía tenemos, pero están por debajo del límite de seguridad. Es nuestra zona de advertencia.
    *   🟢 **Saludable (Óptimo)**: Todo lo que tenemos en cantidades suficientes para trabajar con total tranquilidad.
*   **¿Cómo nos ayuda a decidir?**
    Si ves que la dona tiene un trozo rojo o amarillo grande (más del 15%), significa que nuestra cadena de suministro está teniendo problemas. Puede que los proveedores estén tardando en entregar o que las obras estén consumiendo más rápido de lo previsto. Al ver esto, el encargado de compras sabe de inmediato que debe levantar el teléfono y priorizar los pedidos de esos materiales en riesgo antes de que sea tarde.

---

### 2. Consumo por Frente de Obra (Barras Horizontales)
*   **¿Qué nos muestra al primer vistazo?**
    Nos revela de manera muy clara cuál de todas nuestras obras se está llevando la mayor parte de los materiales. Muestra las 5 obras o frentes de trabajo con mayor stock en este momento, ordenadas de mayor a menor.
*   **¿Cómo nos ayuda a decidir?**
    Esto evita que caigamos en el error de "acaparar". Si notas que una sola obra tiene casi todo el material de la empresa mientras las otras están sufriendo por falta de insumos, no hace falta que salgas corriendo a comprar más. Nos ayuda a tomar la sabia decisión de hacer un **traspaso de materiales** de una obra sobreabastecida a otra que está en apuros. Así ahorramos dinero y aprovechamos al máximo lo que ya tenemos comprado.

---

### 3. Alertas vs. Stock Seguro por Prioridad (Barras Agrupadas con Conteo & Drill-down)
*   **¿Qué nos muestra al primer vistazo?**
    Este gráfico pone frente a frente los materiales que están seguros (en verde) y los que están en peligro de agotarse (en rojo), pero organizados por su nivel de importancia para nosotros: **CRÍTICA**, **MEDIA** y **NORMAL**.
*   **¿Cómo nos ayuda a decidir?**
    Nos ayuda a poner el foco en lo que de verdad importa. Si vemos barras rojas muy altas en la categoría **CRÍTICA**, significa que estamos descuidando los insumos más vitales para la constructora. Lo mejor de todo es que este gráfico es **interactivo (Drill-down)**: si ves una barra roja preocupante, simplemente **haz clic sobre ella**. Al hacerlo, se abrirá una ventana emergente detallada que te dirá exactamente cuáles son esos materiales en alerta, con sus números de vale, en qué obra están y cuántas unidades nos faltan para estar seguros. ¡Es una herramienta quirúrgica para comprar exactamente lo necesario en un par de clics!

---

### 4. Balance Logístico de Flujo (Pie)
*   **¿Qué nos muestra al primer vistazo?**
    Nos permite ver la balanza de nuestro almacén: cuántos materiales están ingresando por compras (**Entradas**) frente a cuántos estamos despachando hacia las obras civiles (**Salidas**).
*   **¿Cómo nos ayuda a decidir?**
    Nos avisa si nos estamos quedando sin reservas. Si vemos que la rebanada de las *Salidas* es gigantesca comparada con la de las *Entradas*, significa que estamos consumiendo nuestro stock mucho más rápido de lo que lo estamos reponiendo. Es una alerta temprana formidable: nos está diciendo que, si no compramos insumos pronto o reducimos el ritmo de despacho, en las próximas semanas nos quedaremos con el almacén completamente vacío.

---

## 🛠️ Stack Tecnológico

* **Backend**: Flask (Python 3.11), SDK de Google Cloud BigQuery, Pandas (para modelado analítico).
* **Frontend**: HTML5, Vanilla CSS3 (estilo premium Glassmorphic optimizado para diseño ergonómico de alto contraste), JavaScript (ES6+), y **Chart.js** para visualización analítica interactiva de gráficos.
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

Para garantizar un 100% de éxito en la ingesta de telemetría IoT transmitida desde dispositivos ESP32 en Wokwi (o simulada desde la cabina del sensor), el backend en `app.py` implementa un flujo híbrido robusto de inserción:
1. **Streaming Ingestion (`insert_rows_json`)**: Primero intenta insertar filas directamente en el búfer de streaming de BigQuery de manera síncrona.
2. **Fallback SQL DML (`INSERT INTO ... VALUES`)**: Si la API de streaming rechaza la transacción por retrasos de propagación o límites de cuota temporales (común en datasets recién creados), el sistema atrapa el error de forma segura y ejecuta una sentencia SQL DML de inserción a través de un Query Job tradicional.

---

## 🔌 Integración IoT: Ingesta de Datos en Vivo con Wokwi (ESP32)

El ecosistema está diseñado bajo una arquitectura IoT moderna. En lugar de depender de registros manuales en oficina, la ingesta de datos ocurre automáticamente desde los frentes de obra a través de microcontroladores **ESP32** simulados en **Wokwi**. 

### 📡 ¿Cómo funciona la arquitectura IoT?
1. **Sensado y Captura (Wokwi)**: El microcontrolador ESP32 simula lecturas continuas de sensores de peso, ultrasonido de volumen o escaneo de códigos de barra RFID en el almacén de obra.
2. **Transmisión de Telemetría (POST HTTP)**: El ESP32 se conecta a la red simulada y realiza peticiones `POST` a la pasarela REST API `/api/data` del servidor Flask con formato JSON cifrado conteniendo los datos de movimiento.
3. **Persistencia en BigQuery**: El servidor Flask recibe el payload de telemetría, valida el esquema y lo inserta en tiempo real en la tabla de **Google BigQuery** (utilizando el mecanismo de fallback resiliente).
4. **Visualización en Tiempo Real**: El dashboard refresca sus gráficos de forma automatizada al detectar nuevos movimientos ingresados por los dispositivos IoT.

### 📝 Ejemplo de Código ESP32 (Arduino C++) para Wokwi:
Puedes simular el hardware IoT utilizando el siguiente sketch en tu simulación de Wokwi para enviar telemetría en tiempo real:

```cpp
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

const char* ssid = "Wokwi-GUEST";
const char* password = "";
const char* serverUrl = "https://control-inventarios-c0f821cf.a.run.app/api/data"; // Reemplazar con tu URL de Cloud Run

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConectado a WiFi Wokwi!");
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverUrl);
    http.addHeader("Content-Type", "application/json");
    
    // Simular lectura de sensor (ej. entrada de cemento a Bodega Norte)
    StaticJsonDocument<256> doc;
    doc["nro_vale"] = "VALE-IOT-" + String(random(1000, 9999));
    doc["fecha_registro"] = "2026-05-28";
    doc["item_material"] = "CEMENTO SOL PORTLAND TIPO I";
    doc["familia_material"] = "AGREGADOS Y CEMENTOS";
    doc["flujo_almacen"] = "ENTRADA";
    doc["cantidad_transaccion"] = 50; // 50 bolsas simuladas
    doc["existencia_anterior"] = 120;
    doc["existencia_actual"] = 170; // 120 + 50
    doc["inventario_seguridad"] = 60;
    doc["estado_disponibilidad"] = "DISPONIBLE";
    doc["frente_o_bodega"] = "BODEGA NORTE";
    doc["unidad_control"] = "BOLSA";
    doc["prioridad_abastecimiento"] = "MEDIA";
    doc["concepto_logitico"] = "INGRESO POR LOTE IoT";
    
    String requestBody;
    serializeJson(doc, requestBody);
    
    int httpResponseCode = http.POST(requestBody);
    
    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.println("Código HTTP: " + String(httpResponseCode));
      Serial.println("Respuesta Servidor: " + response);
    } else {
      Serial.println("Error en la transmisión de telemetría IoT");
    }
    http.end();
  }
  
  // Transmitir cada 30 segundos
  delay(30000);
}
```

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

---
