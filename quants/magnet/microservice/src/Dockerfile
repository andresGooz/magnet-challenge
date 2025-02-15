# Usa la imagen base de Python
FROM python:3 AS builder  

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app  

# Copia solo los archivos necesarios para instalar las dependencias primero (para optimizar el cacheo)
COPY requirements.txt ./

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos de la aplicación
COPY . .

# Exponer el puerto en el que Django corre (por defecto es 8000)
EXPOSE 8000

# Comando para iniciar el servidor
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
