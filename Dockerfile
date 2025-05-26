# Usa una imagen base ligera de Python
FROM python:3.12-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia todos los archivos del proyecto al contenedor
COPY . /app

# Instala las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto que usará Flask (si usas 5000 en app.py)
EXPOSE 5000

# Comando que se ejecutará al iniciar el contenedor
CMD ["python", "app.py"]
