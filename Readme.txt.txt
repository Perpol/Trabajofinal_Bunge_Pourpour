Integrantes del Proyecto BlogSport: Fernando Bunge y Leonel Pourpour

Participacion de Fernando en el proyecto: Back-End
CRUD (en panel de administracion)
LOGIN/LOGOUT
Registro
Utilizacion de Ckeditor
CRUD de usuarios mediante template
Clase POST (Funciona solamente desde panel de admin, la clase en si genera un blog con los elementos del mismo)[con CRUD desde panel admin]
Login Requeriment(permisos de acceso al blog por usuario)


Participacion de Leonel en el proyecto: Front-End
Creacion de Templates bootstrap by layoutit.com
Herencia de Templates
Aplicacion de Mensajeria
Redireccion/Diseño de botones y desplegables.
Configuracion de rutas


REQUISITOS de SOFTWARE PARA EL USO DE BLOGSPORT

asgiref==3.5.2
bootstrap4==0.1.0
distlib==0.3.4
Django==4.0.5
django-ckeditor==6.4.2
django-js-asset==2.0.0
filelock==3.7.1
Pillow==9.2.0
platformdirs==2.5.2
six==1.16.0
sqlparse==0.4.2
tzdata==2022.1
virtualenv==20.15.0

Detalle:
Para que funcione el blog correctamente, descargar la carpeta "Trabajofinal" hacia una ruta identificable en su ordenador personal. Luego mediante su editor de codigo, explore las carpetas y situese en la ruta en donde se encuentre la carpeta descargada e ingrese. Una vez dentro del proyecto debe correr los comandos necesarios para crear la base de datos en su ordenador:
python manage.py makemigrations
python manage.py sqlmigrate AppPlantillas 0001
python manage.py migrate
Una vez finalizado, ejecute el archivo "manage.py". En python el comando es "python manage.py runserver".
Si cumple con todos los requisitos establecidos anteriormente, va a poder utilizar la aplicacion correctamente.
