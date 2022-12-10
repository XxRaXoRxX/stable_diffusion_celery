# Diseño del Sistema (Español):
## Client:
La idea del cliente es que no tenga que instalar nada, sino que ejecute el **boot** y listo, ingrese un prompt y obtenga la imagen, es por eso que no hay requerimientos ni ningún **install** en la carpeta, siempre y cuando tenga Python en su pc, sino va tener que instalarlo.
El cliente se comunica mediante socket, con el servidor, enviando el prompt, y quedándose bloqueado esperando respuesta, es decir, esperando la imagen. Se hizo de esta manera para que no pueda escribir muchos prompt y sobrecargar el Celery con peticiones.

## Server:
El servidor facilita la comunicación entre el cliente y el Celery, la idea principal del servidor, es evitar el uso intensivo del Celery por prompts repetidos, lo que hace el servidor es almacenar las imágenes mediante su prompt, y en caso de que un cliente pida un prompt almacenado en la base de datos, se lo devuelva al instante, y no es necesario mandar información al Redis y Celery evitando trabajo innecesario.
El servidor se maneja mediante Concurrent Futures e hilos, utilizando hilos para responder a múltiples clientes al mismo tiempo, se hizo de esta manera y no por procesos, porque las peticiones son de entrada y salida, no se necesita procesamiento ningún, solo el envió de datos del cliente al Redis y al revés.

## Redis y Celery:
El Redis es el encargado de enviar la tareas a los Workers (Celery), y estos deben recibir el prompt y realizar el trabajo y devolver la imagen, se planteo Celery, para poder aumentar la capacidad de Workers sin problemas en caso de tener muchos clientes que pidan imágenes, conectando nuevos Workers a la red, además de dejar al cliente fuera del trabajo duro y que no note eso, sino que los Workers con su poder de computo hagan el trabajo generando imágenes.
Se utilizo Stable Diffusion, porque es un generador de imágenes mediante prompt Open Source. Por lo cual se han creado muchos repositorios donde se pueden generar imágenes sin necesidad de mucho poder de computo, las demás inteligencias artificiales piden 16gb mínimo de VRam, Stable Diffusion pide 12 VRam, y la comunidad han logrado disminuirlo a 4 VRam, hasta afirman que puede correrlo una placa de video de 2 VRam, perdiendo calidad en el proceso, pero funcionando sin problemas. Yo de momento lo he probado en una 2060 con 6 VRam. Además de la posibilidad de entrenar el modelo con imágenes propias, generar imágenes sin censura (aunque esto se pierde en la versión 2.0) dando muchas posibilidades.

# System Design (English):
## Client:
The idea of the client is that you don't have to install anything, you just run the **boot** and that's it, enter a prompt and get the image, that's why there are no requirements or any **install** in the folder, as long as you have Python on your pc, otherwise you will have to install it.
The client communicates via socket with the server, sending the prompt, and getting stuck waiting for a response, that is, waiting for the image. It was done this way so that it cannot write many prompts and overload Celery with requests.

## Server:
The server facilitates the communication between the client and the Celery, the main idea of the server, is to avoid the intensive use of the Celery by repeated prompts, what the server does is to store the images through its prompt, and in case a client requests a prompt stored in the database, it returns it instantly, and it is not necessary to send information to the Redis and Celery avoiding unnecessary work.
The server is managed by Concurrent Futures and threads, using threads to respond to multiple clients at the same time, it was done this way and not by processes, because the requests are input and output, no processing is needed, only the sending of data from the client to Redis and the other way around.

## Redis and Celery:
The Redis is in charge of sending the tasks to the Workers (Celery), and these must receive the prompt and perform the work and return the image, Celery was raised, to be able to increase the capacity of Workers without problems in case of having many clients that request images, connecting new Workers to the network, besides leaving the client out of the hard work and that he does not notice that, but that the Workers with their computing power do the work generating images.
Stable Diffusion was used, because it is an image generator through Open Source prompt. For which many repositories have been created where images can be generated without the need of much computing power, the other artificial intelligences ask for 16gb minimum of VRam, Stable Diffusion asks for 12 VRam, and the community has managed to reduce it to 4 VRam, they even affirm that a 2 VRam video card can run it, losing quality in the process, but working without problems. I have so far tested it on a 2060 with 6 VRam. In addition to the possibility of training the model with own images, generate uncensored images (although this is lost in version 2.0) giving many possibilities.
