# Cosas que mejorar (Español):
## Client:
- Por parte del cliente se puede agregar mas opciones, como tamaño de imagen, la seed que quieran utilizar.
- Tener mas opciones como img2img, entre otros.
- Una mejor interfaz utilizando alguna página web.
## Server:
- Mejor sistema de almacenamiento de los datos, mediante uso de MYSQL, pudiendo filtrar búsquedas y devolviendo diferentes tipos de imagenes por prompt.
- Mejorar el sistema de conexión de usuarios no solo utilizando hilos, sino agregar **async**, asi puede almacenar mayor cantidad de clientes por hilos.
## Redis:
- Que el usuario pueda cambiar el puerto mas fácilmente, y no tenga que entrar al **boot** y al código para cambiarlo.
## Celery:
- Responder a los cambios planteados por el usuario, según cambio de seed, tamaño de imagen, etc. 
- Que el usuario tenga un **config** con el tamaño de la imagen por default de imagen a crear y la conexión con el Redis. Actualmente esta muy hardcodeado el tema de la configuración.

## Things to improve (English):
## Client:
- On the client side you can add more options, such as image size, the seed they want to use.
- Have more options like img2img, and others.
- A better interface using some web page.
## Server:
- Better data storage system, by using MYSQL, being able to filter searches and returning more types of images by prompt.
- Improve the user connection system not only using threads, but add **async**, so you can store more clients per thread.
## Redis:
- Let the user can change the port more easily, and not have to go into **boot** and code to change it.
## Celery:
- Respond to changes raised by the user, according to seed change, image size, etc. 
- That the user has a **config** with the size of the default image to create and the connection with the Redis. At the moment is very hardcoded the subject of the configuration.