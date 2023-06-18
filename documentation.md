creamos el entorno virtual con virtualenv
pip install virtualenv
virtualenv env
desde la consola entramos a la carpara env, ahi a la carpeta scripts y ahi colocamos activate y enter

###########################################################################################################################
instalamos todas las dependencias que vamos a utilizar que estan listados en requirements.txt
desde nuestra raiz ejecutamos
pip install -r requirements.txt

###########################################################################################################################
creamos un archivo git ignore y vamos a ir colocando ahi los elementos de nuestro proyecto que no queremos que se pusheen a nuestro repo de github

###########################################################################################################################
creamos el proyecto de django con django-admin startprojects social_network
creamos las apps que necesitemos

###########################################################################################################################
creamos una carpeta llamada templates que ahi es donde vamos a alojar todos los templates de nuestro proyecto
dentro de esa carpeta creamos el archivo base.html
creamos una carpeta llamada pages que ahi vamos a colocar todos los templates de nuestras paginas
creamos el archivo index.html
modificamos en el archivo setting.py en el apartado de template colocamos 'DIRS': [os.path.join(BASE_DIR,'templates')],

###########################################################################################################################
instalamos postgresSql
creamos una base de datos con el nombre de nuestro proyecto
en el archivo setting.py en el apartado de databases modificamos los datos colocando
DATABASES = {
'default': env.db("DATABASE_URL", default="postgres://social_network"),
}
DATABASES['default']["ATOMIC_REQUESTS"] = True
que va a hacer referencia a nuestra base de datos PostgresSql, y DATABASE_URL es la variable que va a contener nuestros datos sensibles de ingreso a la DB que eso lo vamos a colocar en el archivo .env
DATABASE_URL=postgres://postgres:password@127.0.0.1:5432/nombreDB

###########################################################################################################################
en el archivo setting.py agregamos unos parametros para que nuestras contraseñas sean mas seguras (contraseñas encriptadas) insertando las siguientes lineas de codigo (aca es donde utilizamos argon2-cffi que los intalamos al principio dentro del archivo requirements.txt)
PASSWORD_HASHERS = [
# https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
"django.contrib.auth.hashers.Argon2PasswordHasher",
"django.contrib.auth.hashers.PBKDF2PasswordHasher",
"django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
"django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

###########################################################################################################################

modificamos en setting.py la parte de static colocandole la ruta local y haciendo una funcion que nos permita mas adelante consumir los datos desde la nube
insertamos todas las configuraciones que nos van a permitir trabajar en la nube de aws con s3
creamos en nuestra app central el archivo storage_bacends.py que es con el que vamos a consumir los datos de la nube

###########################################################################################################################
instalamos tailwindcss usando su documentacion oficial de isntalacion en https://django-tailwind.readthedocs.io/en/latest/installation.html
python -m pip install django-tailwind
agregamos 'tailwind', a nuestras apps
corremos python manage.py tailwind init --> le damos enter
se nos crea una nueva carpeta llamada theme
agregamos 'theme', a nuestras app
agregamos las siguientes variables

     TAILWIND_APP_NAME = 'theme'
     INTERNAL_IPS = [
        "127.0.0.1",
        ]
    colocamos nuestra ruta donde esta instalada npm esto lo podemos ver con el comando where npm y la insertamos en nuestro ptoyecto de la siguiente manera
        NPM_BIN_PATH = r"ruta\de\acceso\npm.cmd"
    corremos el siguiente comando >> python manage.py tailwind install

###########################################################################################################################

realizamos el migrate a nuestra base de datos corremos el comando
python manage.y migrate

corroboramos que en nuestra base de datos se hayan creado las tablas correctamente

###########################################################################################################################

en nuestra app principal creamos el archivo views.py que es donde vamos a crear la vista de nuestra pagina principal (homeView)

agregamos esta vista en el archivo urls.py
path("", HomeView.as_view(), name="home")

###########################################################################################################################

corremos el comando
python manage.py tailwind start
para ver si tailwind esta funcionando correctamente
y si no nos salta ningun error ya podemos correr nuestro servidor y empezar a ver los cambios

###########################################################################################################################
en el archivo setting.py agregamos el siguiente codigo para que RENDER nos funcione bien el astericos de ALLOWED_HOST significa que se va a poder acceder desde cualquier url pero cuando estemos en despliegue debemos colocar nuestro dominio
ALLOWED_HOSTS = [
'*'
]

    RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
    if RENDER_EXTERNAL_HOSTNAME:
        ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

###########################################################################################################################
agregamos las siguientes lineas de codigo en el archivo urls.py para que el sistema cuando este trabajando en debug para trabajar con los static y los media

    from django.conf import settings
    from django.conf.urls.static import static

if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

###########################################################################################################################
Los estilos de facebook se obtuvieron del siguiente repositorio de github
https://github.com/trananhtuat/tailwindcss-facebook

en el archivo tailwind.config.js agregamos colores y variaciones de estilos para trabajar con otros colores y con el modo oscuro

    darkMode:'media',
    theme: {
        extend: {
            'dark-main': '#18191A',
            'dark-second': '#242526',
            'dark-third': '#3A3B3C',
            'dark-txt': '#B8BBBF',
            sky: colors.sky,
            teal: colors.teal,
            rose: colors.rose,
        },
    },

    variants: {
        extend: {
            display: ['group-hover'],
            transform: ['group-hover'],
            scale: ['group-hover'],
            textOpacity: ['dark'],
        },
    },

en la carpeta static_src de theme vamos a instalar un paquete de taildwind con el siguiente comando
la instalacion esta descripta en la web oficial https://www.npmjs.com/package/tailwind-scrollbar-hide
npm install tailwind-scrollbar-hide
y agregamos <require('tailwind-scrollbar-hide')> en los plugins del archivo taildwind.config

este plugins nos sirve para eliminar las barras de scroll

###########################################################################################################################
colocamos en nuestro head
<!--AlpineJS-->
<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.8.2/dist/alpine.min.js" defer></script>

    <!--Boxicons-->
    <link href='https://unpkg.com/boxicons@2.0.7/css/boxicons.min.css' rel='stylesheet'>

    <!--JQuery-->
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.min.js"></script>

    alpine.js es para trabajar con intercambio de vistas y boxicons para trabajar con iconos

###########################################################################################################################
instalamos allauth para trabajar los login, seguimos los pasos de instalacion de su web oficial
https://django-allauth.readthedocs.io/en/latest/installation.html

y realizamos una migracion de nuestro proyecto con el python manage.py migrate

###########################################################################################################################
creamos un superusuario para acceder al panel de administrador de django

###########################################################################################################################
creamos el login y el crear cuenta utilizando el template que nos brinda la documentacion oficial de allauth y con django-crispy web oficial https://django-crispy-forms.readthedocs.io/en/latest/install.html

django-crispy es una libreria que nos ofrece formularios predeterminados
instalamos crispy-tailwind para a esas librerias darle estilos con tailwind

se creo templates para mostrar las confirmaciones de email al crear la cuenta

###########################################################################################################################

creamos la app users para ahi guardar todos las cuentas de los usuarios
y en vistas extendemos de django.contrib.auth.models la clase AbstractUser que es donde django nos da todos los elementos necesarios para crear un usuario base
despues usamos django.conf para poder configurar la autenticacion de los usuarios
despues usamos PIL para el procesamiento de imagenes

creamos la carpeta media/img y ahi adentro colocamos la imagen de perfil y banner por defecto que se crea cuando creamos un nuevo usuario

se creo los templates para el perfil del usuario
se creo el template para editar el perfil de usuario y se edito el views.py para agregar la logica para poder modificar los datos del usuario

######################################################################################################

en la app social en el archivo models.py creamos las clases para poder crear los posteos y comentarios
y en el archivo forms.py creamos el formulario para crear un nuevo post

se modifico el archivo index.html de la carpeta pages
hicimos las migraciones de social y user

se creo la carpeta posts en la ruta templates/pages
con los archivos delete.html y edit.html que van a ser los template para cuando querramos editar o borrar una publicación

en el archivo views.py se creo la logica para editar y borrar las publicaciones utilizando UpdateView, DeleteView

##################################################################################################

se creo la logica para seguir y dejar de seguir a un usuario.
se creo la logica para ver los seguidores, el template, se configuro la url pero no encuentro el error por el cual no me lo muestra al template.
