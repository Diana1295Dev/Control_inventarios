# 🏗️ Dashboard Inteligente de Control de Inventarios para Constructoras

Este es un dashboard premium interactivo y en tiempo real diseñado específicamente para la analítica de datos logísticos, control de abastecimiento y prevención de quiebres de obra en empresas de construcción mediante ingesta de datos en tiempo real. La aplicación se conecta de forma nativa a **Google BigQuery** utilizando un backend robusto en Flask (Python) y una interfaz de usuario glassmórfica premium impulsada por **Chart.js** para visualización analítica avanzada.

---

## 👥 Estructura del Equipo de Exposición y Roles

Para la presentación del proyecto ante evaluadores, el equipo se divide estructuradamente en **4 integrantes** desde el inicio, cada uno enfocado en un pilar clave del desarrollo técnico:

| 👤 Integrante | 🛠️ Especialidad & Rol | 📋 Temas de Exposición |
| :--- | :--- | :--- |
| **Integrante 1** | Líder de Proyecto & Diseñador UX/UI | Introducción del problema logístico, propuesta de valor de negocio, estética Glassmorphic corporativa de alto contraste y baja fatiga visual y ingesta e integración de flujos de datos de telemetría IoT. |
| **Integrante 2** | Arquitecto de Software & Backend | Backend en Flask (Python), Gateway API/REST IoT, conector nativo con Google BigQuery y arquitectura de persistencia con doble ruta de respaldo (Streaming + Fallback SQL). |
| **Integrante 3** | Analista de Datos & Especialista en BI | Dashboards interactivos en Chart.js, análisis estadístico dual (Descriptivo e Inferencial) de las 4 métricas clave e interactividad avanzada Drill-down (clic en barras para abrir detalles). |
| **Integrante 4** | Ingeniero de DevOps & Cloud Computing | Flujo de control de versiones limpio en Git, contenedorización con Docker, despliegue serverless en Google Cloud Run y seguridad de credenciales IAM de Google Cloud. |

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

## 🎤 Guion de Exposición – Dashboard Inteligente de Control de Inventarios para Constructoras

Este guion interactivo está diseñado para que **4 integrantes** puedan presentar de forma coordinada, profesional y detallada la solución completa ante evaluadores o clientes.

---

### 👤 INTEGRANTE 1 – Líder de Proyecto, UX/UI y Contexto del Problema

**Tema: Introducción, problemática, propuesta de valor y experiencia de usuario**

> *"Buenos días a todos.
> 
> Hoy presentamos nuestro proyecto: **Dashboard Inteligente de Control de Inventarios para Constructoras**, una solución diseñada para resolver uno de los mayores problemas operativos del sector construcción: el desabastecimiento de materiales críticos en frentes de obra.
> 
> Cuando materiales como cemento, acero o tuberías no llegan a tiempo, las obras se detienen, se generan retrasos, sobrecostos y pérdidas económicas importantes para la empresa.
> 
> Nuestra propuesta busca transformar el inventario tradicional en un sistema inteligente de datos en tiempo real, capaz de monitorear materiales continuamente, detectar riesgos y apoyar la toma de decisiones.
> 
> Desde la perspectiva de experiencia de usuario diseñamos una interfaz moderna basada en **Glassmorphism corporativo de alto contraste y baja fatiga visual**, buscando que el usuario pueda interpretar grandes volúmenes de información de manera rápida y ergonómica.
> 
> Entre las principales funcionalidades encontramos:
> 
> • Visualización centralizada de inventarios analíticos.
> • Paneles interactivos para análisis de demanda y consumo logístico.
> • Monitoreo en tiempo real de movimientos de materiales.
> • Integración con pasarelas de telemetría IoT para recepción automática de información.
> • Modal interactivo que permite visualizar materiales críticos con desglose de déficit a nivel de vale.
> 
> Con esto buscamos que la plataforma no solo muestre datos, sino que permita actuar rápidamente frente a problemas operativos cotidianos.
> 
> Ahora le doy paso a mi compañero para explicar cómo construimos la arquitectura tecnológica que soporta toda esta solución."*

---

### 👤 INTEGRANTE 2 – Arquitecto de Software y Backend

**Tema: Backend, APIs, BigQuery e ingestión de datos resiliente**

> *"Muchas gracias.
> 
> Para soportar esta solución construimos una arquitectura backend utilizando **Python y Flask**, priorizando rendimiento, simplicidad y escalabilidad empresarial.
> 
> Nuestra arquitectura se compone principalmente de tres elementos analíticos:
> 
> Primero, desarrollamos una **API REST** que funciona como punto central de comunicación segura entre el frontend, la base de datos y las fuentes de telemetría en bodega.
> 
> Segundo, utilizamos **Google BigQuery** como motor analítico principal a escala de petabytes, permitiéndonos almacenar e interrogar grandes volúmenes de datos de forma sumamente veloz.
> 
> Tercero, implementamos **mecanismos de ingestión resilientes** para garantizar la persistencia de datos bajo cualquier circunstancia.
> 
> Nuestro sistema expone tres endpoints principales:
> • `/api/status` → valida conexiones y el estado del sistema con la nube de Google.
> • `/api/data` → recibe y consulta los movimientos de inventario en tiempo real.
> • `/api/stats` → genera agregaciones analíticas instantáneas para alimentar los gráficos.
> 
> Para garantizar la confiabilidad de los flujos continuos de datos, implementamos un **esquema híbrido de inserción**:
> Inicialmente intentamos insertar registros mediante streaming. Si ocurre alguna congestión o falla temporal de red, el sistema activa automáticamente un mecanismo alternativo basado en consultas SQL tradicionales. Esto permite mantener la persistencia y la integridad de los datos de inventario incluso ante escenarios de alta concurrencia de transacciones.
> 
> Ahora veremos cómo convertimos estos datos en información útil para el negocio."*

---

### 👤 INTEGRANTE 3 – Analista de Datos y Business Intelligence

**Tema: KPIs, métricas y lectura descriptiva de gráficos para toma de decisiones**

> *"Gracias.
> 
> Nuestro enfoque analítico se centró en transformar datos operativos crudos en **indicadores de alto impacto y visualizaciones accionables** para la toma de decisiones logísticas rápidas.
> 
> El dashboard calcula y actualiza cuatro métricas clave en tiempo real:
> • **Total de movimientos logísticos**: para entender la dinámica transaccional global.
> • **Stock total disponible**: que nos da la suma física absoluta de nuestro inventario en bodega.
> • **Nivel de servicio de obra**: un indicador vital en porcentaje que mide cuántas transacciones operan de forma segura por encima del inventario mínimo.
> • **Alertas activas y materiales críticos**: que avisa de inmediato cuántos insumos estratégicos requieren compra urgente.
> 
> Pero el verdadero valor analítico está en nuestras cuatro visualizaciones, diseñadas bajo un enfoque descriptivo y funcional:
> 
> **1. Salud del Inventario (Gráfico de Dona)**
> Clasifica nuestros materiales en tres estados de disponibilidad: **Crítico (Agotado)** en rojo, **Riesgo (Bajo Mínimo)** en amarillo y **Saludable** en verde. 
> *¿Cómo nos ayuda a decidir?* Este gráfico funciona como un termómetro de la cadena de suministro. Si el área roja y amarilla supera el 15%, deducimos de inmediato que tenemos problemas de inestabilidad en las entregas de los proveedores o aceleraciones bruscas de consumo en obra. Esto le advierte al gerente que debe priorizar y acelerar órdenes de compra de inmediato.
> 
> **2. Consumo por Frente de Obra (Barras Horizontales)**
> Muestra las 5 obras o frentes de trabajo con mayor stock en este momento.
> *¿Cómo nos ayuda a decidir?* Nos permite detectar desequilibrios en la asignación de materiales. Si una sola obra concentra el 70% del inventario general mientras las demás sufren escasez, deducimos un acaparamiento localized e ineficiente. Esto nos permite decidir realizar un **traspaso de materiales inter-obras**, optimizando el capital de trabajo ya invertido sin gastar en compras redundantes.
> 
> **3. Alertas vs. Stock Seguro por Prioridad (Barras Agrupadas con Drill-down)**
> Compara los materiales seguros contra los que están en peligro de agotarse, organizados por prioridad: **CRÍTICA**, **MEDIA** y **NORMAL**.
> *¿Cómo nos ayuda a decidir?* Mide la efectividad real de nuestra política de abastecimiento. Si vemos alertas rojas muy altas en la categoría **CRÍTICA**, deducimos una falla en el reabastecimiento de insumos estratégicos. La gran ventaja es que incorporamos interactividad **Drill-Down**: al hacer clic en una barra en peligro, el sistema nos abre un modal detallado con la lista exacta de los materiales en quiebra, sus vales, ubicación y el déficit de unidades exacto para reponerlos de inmediato.
> 
> **4. Balance Logístico (Gráfico de Pie)**
> Compara los flujos de Entrada (abastecimientos) contra los flujos de Salida (consumo de las obras).
> *¿Cómo nos ayuda a decidir?* Mide la velocidad de agotamiento de nuestro almacén central. Si notamos que las Salidas superan de manera persistente a las Entradas, deducimos que consumimos el stock a un ritmo insostenible. Esta alerta temprana nos indica que el almacén se quedará completamente vacío en las próximas semanas si no inyectamos capital de trabajo o reprogramamos compras.
> 
> Nuestro objetivo fue convertir información compleja en visualizaciones simples, intuitivas y accionables para que el gerente actúe antes de que la obra se detenga.
> 
> Ahora veremos cómo logramos desplegar todo esto en la nube de forma segura y portable."*

---

### 👤 INTEGRANTE 4 – DevOps, Cloud e Infraestructura

**Tema: Git, Docker, Cloud Run y seguridad sin llaves**

> *"Muchas gracias.
> 
> Para asegurar que esta solución fuera escalable, altamente portable y segura en la nube implementamos prácticas DevOps modernas de primer nivel.
> 
> Primero, utilizamos **Git** para control de versiones, implementando un `.gitignore` estricto que protege el código de fugas accidentales de configuraciones sensibles locales.
> 
> Posteriormente dockerizamos toda la aplicación escribiendo un **Dockerfile optimizado**. Esto nos permitió garantizar la consistencia absoluta del entorno de ejecución, asegurando que el sistema funcione exactamente igual tanto en ambientes de desarrollo local como en producción en la nube.
> 
> El proceso de despliegue continuo se realizó utilizando **Google Cloud Platform** mediante:
> • **Cloud Build** para la construcción automatizada de contenedores.
> • **Artifact Registry** para el almacenamiento de imágenes seguras.
> • **Cloud Run** para la ejecución serverless del backend.
> 
> Cloud Run nos ofrece ventajas operativas gigantescas: escalabilidad automática e instantánea según la demanda, cobro exacto únicamente por tiempo de procesamiento de peticiones, alta disponibilidad en múltiples zonas, y capacidad de escalar hasta cero cuando no existen usuarios conectados, reduciendo los costos operativos a cero.
> 
> Finalmente, implementamos un modelo de seguridad altamente robusto basado en **Google Cloud IAM (Identity and Access Management)**. De esta forma, evitamos por completo almacenar claves o archivos JSON físicos de credenciales dentro del contenedor; en su lugar, asignamos permisos dinámicos directos a la Service Account de Cloud Run. El sistema se conecta de forma nativa a BigQuery sin llaves expuestas, garantizando una arquitectura impenetrable.
> 
> Con esto logramos construir una solución completa: analítica, escalable, ergonómica, automatizada y lista para operar en tiempo real. Quedamos atentos a sus dudas. ¡Muchas gracias!"*
