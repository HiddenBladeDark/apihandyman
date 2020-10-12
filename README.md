# HandyManAPI

# 1. Para instalar proyecto usar un ambiente virtual de python usando el comando /virtualenv <nombre_del_ambiente>.

# 2. Luego de tener el ambiente virtual instalado, activalo si usas linux:
       entrar a la carpeta de scripts 
       source activate
  en caso de que uses windows usando el CMD solo es usar:
      - .\Scripts\Activate

# 3. Una vez que este el ambiente activado clonar el repositorio con:
      git clone https://github.com/HiddenBladeDark/apihandyman

# 4. entrar al repositorio e instalar las librerias requeridas usando el comando:
       pip install -r requirements.txt

# TENER MYSQL SERVER INSTALADO EN EL EQUIPO O CAMBIAR LA CADENA DE CONEXION EN SETTINGS.PY PARA USAR DB PREFERIDA

# 5. Usar los comandos para :
      python manage.py makemigrations
      python manage.py migrate

# 6. Correr el servidor con:
      python manage.py runserver
