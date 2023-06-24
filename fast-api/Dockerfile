#Aqui va la version de python a utilizar
FROM python:3.10

# esta es la carpeta donde se va a guardar el proyecto que vamos a correr rn docker
WORKDIR /app

#copiamos el archivo local de las dependencias y lo copiamos a la carpeta que recien creamos (/app)
COPY requirements.txt /app/requirements.txt

#aqui instalamos las dependencias que antes copiamos
RUN pip3 install --no-cache-dir --upgrade -r /app/requirements.txt

#aqui le decimos que copie la carpeta actual (.) en nuestra carpeta (/app)
COPY . /app

#este comando mantiene encendido el contenedor docker
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
