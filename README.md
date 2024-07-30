# Proyecto de Gestión de Usuarios y Contenidos en Django

## Descripción

Este proyecto es una aplicación web diseñada para gestionar usuarios y contenido multimedia relacionado con varias bandas de música. Incluye funcionalidades de registro, inicio de sesión, recuperación de contraseña, modificación de datos de usuario, y varias vistas para mostrar información de diferentes bandas de música. La aplicación está desarrollada con Django y sigue buenas prácticas de seguridad y manejo de usuarios.
## Tecnologías Usadas

- **Backend**:
    - [Django](https://www.djangoproject.com/): Un framework web de alto nivel para el desarrollo rápido de aplicaciones web seguras y mantenibles en Python.
    - [Django ORM](https://docs.djangoproject.com/en/stable/topics/db/queries/): Para la interacción con la base de datos.

- **Frontend**:
    - [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5): Para la estructura del contenido web.
    - [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS): Para el diseño y la presentación visual.
    - [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript): Para la interactividad y el comportamiento dinámico.

- **Base de Datos**:
    - [SQLite](https://www.sqlite.org/index.html): Base de datos ligera utilizada en el desarrollo local.
    - [PostgreSQL](https://www.postgresql.org/): Base de datos relacional avanzada que puede ser utilizada en producción.

- **Autenticación y Autorización**:
    - [Django Auth](https://docs.djangoproject.com/en/stable/topics/auth/): Sistema de autenticación y autorización de Django.

- **Envío de Correos**:
    - [Django Email](https://docs.djangoproject.com/en/stable/topics/email/): Para el envío de correos electrónicos, incluyendo la recuperación de contraseñas.

- **Herramientas de Desarrollo**:
    - [Visual Studio Code](https://code.visualstudio.com/): Editor de código fuente.
    - [Git](https://git-scm.com/): Sistema de control de versiones.
    - [GitHub](https://github.com/): Plataforma de hospedaje de código.

- **Entorno Virtual**:
    - [pipenv](https://pipenv.pypa.io/en/latest/): Herramienta para manejar dependencias de Python y entornos virtuales.

## Características

1. **Gestión de Usuarios**
    - **Registro de Usuarios**: Los usuarios pueden registrarse proporcionando un correo electrónico y otros datos personales. Se verifica si el correo electrónico ya está en uso antes de permitir el registro.
    - **Inicio de Sesión**: Los usuarios pueden iniciar sesión proporcionando su nombre de usuario y contraseña.
    - **Modificación de Datos**: Los usuarios pueden modificar su información personal a través de un formulario.
    - **Recuperación de Contraseña**: Los usuarios pueden solicitar un enlace de restablecimiento de contraseña si olvidan su contraseña.

2. **Gestión de Contenidos**
    - **Bandas de Música**: La aplicación muestra información sobre varias bandas de música, incluyendo Indio Solari, La Renga, Divididos, Ciro, Notvg, y Las Pelotas.
    - **Lugares**: Información sobre diferentes lugares relacionados con las bandas de música.
    - **Imágenes**: Visualización de imágenes relacionadas con las bandas y los eventos.

3. **Formularios de Contacto**
    - **Formulario de Contacto**: Los usuarios pueden enviar mensajes a través de un formulario de contacto. Los mensajes se envían a un correo electrónico específico.

## Estructura del Proyecto

- **Vistas**
    - `home`: Vista principal que muestra la página de inicio.
    - `imagen`: Vista que muestra las imágenes.
    - `RegistroView`: Vista para el registro de usuarios.
    - `InicioSesionView`: Vista para el inicio de sesión de usuarios.
    - `logout_view`: Vista para cerrar sesión.
    - `indio_solari_view`, `la_renga_view`, `divididos_view`, `ciro_view`, `notvg_view`, `las_pelotas_view`: Vistas para mostrar información de diferentes bandas.
    - `modificar_datos_usuario`: Vista para modificar los datos del usuario.
    - `forgot_password`: Vista para la recuperación de contraseña.
    - `FormContacto`: Vista para mostrar el formulario de contacto.
    - `contacto`: Vista para procesar y enviar el formulario de contacto.
    - `gracias`: Vista de agradecimiento después de enviar el formulario de contacto.
    - `QuienesSomos`: Vista que muestra información sobre quiénes somos.

- **Modelos**
    - `Indio_Solari`, `La_renga`, `Divididos`, `Ciro`, `notvg`, `LasPelotas`, `lugares`: Modelos que representan las bandas y los lugares.

- **Formularios**
    - `RegistroForm`, `AuthenticationForm`, `ModificarUsuarioForm`, `PasswordResetRequestForm`, `ContactForm`: Formularios utilizados para registro, inicio de sesión, modificación de datos, recuperación de contraseña y contacto.

## Instalación

1. Clona el repositorio:
    ```bash
    git clone <URL del repositorio>
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd <nombre del proyecto>
    ```
3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
4. Realiza las migraciones:
    ```bash
    python manage.py migrate
    ```
5. Inicia el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría hacer.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.
