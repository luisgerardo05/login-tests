# HOLIS PISTOLIS
Antes que nada verifica si tienes instalado locust, si no te dejo el comando
```
pip3 install locust
```

Ahora debes abrir el archivo con nombre **start.sh** 

Después debes identificar el archivo que deseas ejecutar, los cuales se describen a continuación:

- control.py: se ejecuta una task por ruta que existe en el servicio.
- login.py: se ejecutan tasks que solo se dedican a probar la ruta de login con campos correctos, correo malo, password malo y con un usuario no registrado.
- register.py: se ejecutan tasks que solo se dedican a probar la ruta de register con campos correctos, correo mal escrito y password no verrificado.

*Nota:* El archivo user_data_generator.py sirve como controlador para poder crear información del usuario.

Una vez identifiado el archivo a probar debes descomentar el que elegiste y comentar el resto de comandos.

Para correr esta basura es rotundamente necesario abrir una terminal del proyecto y ejecutar el comando: 
```
bash start.sh
```
