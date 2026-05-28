# Usar la imagen oficial ligera de Python.
FROM python:3.11-slim

# Evitar que Python escriba archivos .pyc en el disco
ENV PYTHONDONTWRITEBYTECODE=1

# Permitir que los mensajes de log se muestren inmediatamente en los logs de la consola
ENV PYTHONUNBUFFERED=1

# Definir el puerto predeterminado (Google Cloud Run inyecta la variable PORT automáticamente)
ENV PORT=8080

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar e instalar las dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente de la aplicación al contenedor
COPY . .

# Exponer el puerto configurado
EXPOSE 8080

# Ejecutar el servidor WSGI Gunicorn en el inicio del contenedor.
# Se configuran 1 worker y 8 hilos (threads) para manejo eficiente de concurrencia.
# Se define un timeout de 0 para delegar la gestión de escalado y timeouts a Cloud Run.
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 app:app
