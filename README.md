# 🏗️ Dashboard Inteligente de Control de Inventarios para Constructoras

Este es un dashboard premium interactivo y en tiempo real diseñado específicamente para la logística, el control de abastecimiento y la prevención de quiebres de obra en empresas de construcción. La aplicación se conecta de forma nativa a **Google BigQuery** utilizando un backend robusto en Flask (Python) y una interfaz de usuario glassmórfica premium impulsada por **Chart.js** para visualización analítica avanzada.

---

## 👥 Estructura del Equipo de Exposición y Roles

Para la presentación del proyecto ante evaluadores, el equipo se divide estructuradamente en **4 integrantes** desde el inicio, cada uno enfocado en un pilar clave del desarrollo técnico:

| 👤 Integrante | 🛠️ Especialidad & Rol | 📋 Temas de Exposición |
| :--- | :--- | :--- |
| **Integrante 1** | Líder de Proyecto & Diseñador UX/UI | Introducción del problema logístico, propuesta de valor de negocio, estética Glassmorphic corporativa de alto contraste y baja fatiga visual y simulación interactiva de sensores IoT en el frontend. |
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

## 🎤 Guión Explicativo para Exposición (Estructura para 4 Expositores)

Este guión interactivo está diseñado para que **4 integrantes** puedan presentar de forma coordinada, profesional y detallada la solución completa ante evaluadores o clientes. Cada sección aborda un pilar del software (Diseño, Backend, Analítica y DevOps).

---

### 👤 INTEGRANTE 1: Líder de Proyecto, Diseño UX/UI e Interacción
**Tema: Introducción, Propuesta de Valor, Diseño Glassmorphism e Interactividad**

> *"Buenos días a todos. Hoy presentaremos nuestro **Dashboard Inteligente de Control de Inventarios para Constructoras**, una plataforma diseñada para resolver un problema crítico en la industria: **el quiebre de stock de materiales en frentes de obra**, el cual paraliza maquinarias, causa sobrecostos y demora los proyectos civiles.*
>
> *Mi rol se centró en la dirección del proyecto y el diseño de la interfaz de usuario (UX/UI). Decidimos alejarnos de los diseños tradicionales y genéricos para implementar una estética **Glassmorphism corporativo de alto contraste** de alta gama. Esto se logra mediante fondos translúcidos, filtros de desenfoque (`backdrop-filter: blur`), gradientes sutiles (tonalidades HSL personalizadas en azules y cianes) y micro-animaciones en los componentes.*
>
> **Características clave que diseñamos para la interacción:**
> 1. **Encabezado Inteligente:** Muestra el logo dinámico y un indicador de estado que verifica síncronamente si la base de datos distribuida en Google BigQuery está conectada.
> 2. **Simulador de Transmisión de Sensores IoT (Wokwi):** En producción, el stock se actualiza automáticamente mediante dispositivos físicos (como básculas, lectores RFID o escáneres de código de barras basados en **ESP32** simulados en **Wokwi**). Para la demostración en vivo, diseñamos un panel interactivo que modela de forma idéntica esta telemetría IoT: al activarse, permite simular la transmisión de una trama de datos de sensor mediante un protocolo POST en caliente a nuestra pasarela analítica, calculando de forma automática el stock y disparando el estado de disponibilidad del material.
> 3. **NUEVA FUNCIONALIDAD - Modal de Desglose de Alertas:** A petición del negocio, implementamos interactividad directa en la tarjeta de alertas. Al hacer clic sobre el card de 'Frentes Activos' que avisa la existencia de stock crítico (por ejemplo, las 54 alertas activas), la interfaz abre un **modal premium translúcido** con el desglose detallado en tiempo real. Esta tabla muestra el número de vale, el material específico, su ubicación (bodega/frente), prioridad, stock actual, stock de seguridad y el **déficit exacto** de unidades faltantes para activar la orden de compra urgente. 
> 
> *Le cedo la palabra a mi compañero para explicar la arquitectura de datos."*

---

### 👤 INTEGRANTE 2: Arquitecto de Software y Backend
**Tema: Backend en Flask, Integración Nativa con BigQuery y Mecanismos de Ingesta Resilientes**

> *"Muchas gracias. Para dar vida a este diseño UX, estructuramos un backend altamente optimizado en **Python** utilizando el framework ligero **Flask**.*
>
> *Nuestra principal meta era asegurar una latencia mínima y una conexión 100% segura con **Google BigQuery**. Para ello, en `app.py` implementamos el SDK oficial de Google Cloud. El sistema utiliza **Application Default Credentials (ADC)** de forma local y hereda la Service Account de forma transparente en la nube, eliminando la necesidad de exponer claves JSON físicas en producción.*
>
> **Desarrollamos una API interna y Pasarela IoT con 3 endpoints clave:**
> 1. `/api/status`: Realiza un ping síncrono a BigQuery validando la existencia de la tabla e identificando el ID del proyecto, dataset y tabla.
> 2. `/api/data`: Recupera de forma paginada y filtrable los últimos registros, y actúa como un **REST IoT Gateway** para procesar las peticiones `POST` enviadas por los microcontroladores ESP32 en Wokwi.
> 3. `/api/stats`: Realiza consultas de agregación analítica de alta velocidad en BigQuery para alimentar el motor de gráficos en el frontend.
>
> **Arquitectura de Ingestión Resiliente para Dispositivos IoT:**
> *Al momento de recibir telemetría IoT desde Wokwi, implementamos una lógica híbrida de tolerancia a fallos única para manejar el flujo continuo de sensores:*
> *   *Primero, intentamos insertar el registro mediante **Streaming Ingestion (`insert_rows_json`)** para lograr disponibilidad inmediata en el buffer de BigQuery.*
> *   *Si la API de BigQuery rechaza la ráfaga de streaming temporalmente por límites de cuota de propagación en la tabla analítica, el backend activa automáticamente un **Fallback a DML tradicional**, ejecutando un Job de inserción directa (`INSERT INTO ... VALUES`). Esto garantiza un **100% de persistencia de datos** de telemetría ante cualquier eventualidad de concurrencia.*
>
> *Ahora, pasaremos a analizar los KPIs y el motor analítico de visualización."*

---

### 👤 INTEGRANTE 3: Especialista en Data Analytics y Visualización
**Tema: Métricas de Negocio (KPIs), Gráficos Estadísticos Clave y Legibilidad de Datos**

> *"Gracias. Mi rol se enfocó en traducir los datos crudos de BigQuery en valor de negocio a través de métricas analíticas e interactividad gráfica impulsada por **Chart.js**.*
>
> *Hemos definido 4 KPIs principales en el panel superior:*
> 1. **Total Movimientos:** Volumen histórico de transacciones logísticas.
> 2. **Stock Total Obra:** Suma absoluta del inventario disponible en toda la organización.
> 3. **Nivel de Servicio de Obra (%):** Esfera clave que mide qué porcentaje de transacciones operan de forma segura por encima del inventario mínimo.
> 4. **Frentes Activos & Alertas:** Alerta visual y cuantitativa parpadeante que avisa cuántos materiales críticos requieren compra urgente.
>
> **Análisis Estadístico y Visualizaciones con Legibilidad de Alto Rendimiento:**
> *Para cumplir con los estándares más exigentes, rediseñamos los gráficos de Chart.js agregando **etiquetas explícitas de ejes**, **leyendas informativas** y **tooltips interactivos con porcentajes calculados dinámicamente**:*
>
> 1. **Gráfico 1: Salud del Inventario (Dona):** Categoriza el stock en tres niveles: *Crítico (Quiebre)*, *En Riesgo* y *Saludable*. Su tooltip dinámico muestra la cantidad exacta de materiales en dicho estado y calcula síncronamente su porcentaje frente al total.
> 2. **Gráfico 2: Consumo por Frente de Obra (Barras Horizontales):** Visualiza los frentes de trabajo o proyectos que concentran la mayor cantidad de recursos. Añadimos títulos claros en los ejes X (*Cantidad en Almacén*) e Y (*Proyectos / Frentes de Obra*) y personalizamos el tooltip para denotar las unidades en stock.
> 3. **Gráfico 3: Alertas vs. Stock Seguro por Prioridad (Barras Agrupadas con Conteo & Drill-down):** Para evitar la trampa de los promedios y porcentajes abstractos, implementamos un gráfico de barras agrupadas (lado a lado) que muestra de forma **directa la cantidad de materiales en Alerta / Quiebre (Rojo)** vs. **Stock Seguro (Verde)** por prioridad (*CRÍTICA*, *MEDIA*, *NORMAL*) con números flotantes exactos encima de cada barra. **Además, implementamos interactividad de nivel empresarial (Drill-Down)**: el usuario puede pasar el mouse (el cursor cambia a pointer) y **hacer clic en cualquier barra** para abrir automáticamente el modal analítico pre-filtrado mostrando la **lista exacta de los materiales** correspondientes a ese segmento con sus vales, frentes y déficits en tiempo real.
> 4. **Gráfico 4: Balance Logístico (Circular/Pie):** Compara las transacciones de entrada contra salida. Sus tooltips desglosan el volumen exacto y la participación porcentual de flujo de entrada/salida.
> 
> *A continuación, revisaremos cómo automatizamos el despliegue e infraestructura."*

---

### 👤 INTEGRANTE 4: Ingeniero de DevOps y Cloud Computing
**Tema: Git Limpio, Contenedorización, Despliegue en Cloud Run e IAM Security**

> *"Muchas gracias. Para asegurar que este sistema sea fácilmente escalable, portable y seguro en la nube, implementamos un flujo de trabajo basado en metodologías **DevOps**.*
>
> **Gestión de Versiones y Git Limpio:**
> *Inicializamos un repositorio robusto en GitHub. Diseñamos un archivo `.gitignore` estricto para evitar la fuga accidental de credenciales locales (`credentials.json`), variables de configuración sensible (`.env`) o dependencias de librerías locales (`venv/`).*
>
> **Contenedorización con Docker:**
> *Escribimos un `Dockerfile` optimizado multicapa. El contenedor empaqueta la app de Flask con todas sus dependencias en un entorno aislado bajo un servidor HTTP para producción (`gunicorn`), garantizando que la aplicación se comporte exactamente igual en local y en la nube.*
>
> **Despliegue Continuo en Google Cloud Platform (GCP):**
> *Implementamos una canalización rápida utilizando comandos de Google Cloud SDK:*
> 1. *Compilamos nuestra imagen de contenedor en la nube de forma segura utilizando **Google Cloud Build**.*
> 2. *La registramos en **Artifact Registry**.*
> 3. *Realizamos el despliegue serverless en **Google Cloud Run**.*
>
> **Configuración de Permisos IAM Seguros en Producción:**
> *Al desplegar en Cloud Run, resolvemos las conexiones a BigQuery de forma óptima. En lugar de adjuntar archivos JSON de credenciales, le otorgamos a la **Service Account de Compute por defecto** de Cloud Run los roles de **BigQuery Data Editor** y **BigQuery Job User** en la consola IAM de GCP. De esta forma, el contenedor hereda los privilegios dinámicamente y se conecta de manera directa e impenetrable.*
>
> *Con esto, concluimos nuestra exposición. Hemos entregado una solución integral: interactiva, analítica, altamente resiliente en BigQuery y automatizada en la nube. Quedamos atentos a sus preguntas. Muchas gracias."*

