# Usa una imagen base de Python
FROM python:3.9

# Crea un directorio de trabajo
WORKDIR /app

# Copia los archivos de la aplicación
COPY . .

# Instala las dependencias
RUN pip install flask

# Ejecuta el servidor
CMD ["python", "app.py"]
