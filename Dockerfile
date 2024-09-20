# Usar una imagen de Python 3.10
FROM python:3.11.4-slim

# Configurar el directorio de trabajo
WORKDIR /app

# Copiar el archivo de dependencias y el código
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

# Exponer el puerto
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["python", "app.py"]