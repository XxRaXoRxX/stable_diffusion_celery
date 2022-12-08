# Installers (English)
## Client:
The client does not ask for any requirements, just keep in mind that everything runs on Python, so you must have [Python](https://www.python.org/downloads/) installed on your operating system, recommended version 3.8 or higher. Run with **boot_linux.sh** or **boot_windows.bat** depending on the operating system, take into account to configure the port and host of the server in **client_config.py**.

<p align="center"><img src="https://i.ibb.co/RbjZY9F/Captura-de-pantalla-2022-12-08-122647.jpg)"/></p>

## Redis:
To run Redis **Docker** must be installed on the operating system, the download links are inside the **install.txt**, once installed Docker, in Windows you must have **Docker** running in the background to run the Redis with **boot_windows.bat**, in linux just running **boot_linux.sh** is enough. The redis runs on port 6379:6379, if you want to change it, go into the executable and edit:

<p align="center"><img src="https://i.ibb.co/wgw4WQN/redis-Config.jpg)"/></p>

## Server:
To run the server you need the requirements inside the **requirements.txt**, keep in mind that to run the server you need [Python](https://www.python.org/downloads/) installed in the operating system, and by just running **install_linux.sh** or **install_windows.bat** depending on your system, the requirements will be installed inside a virtual environment, once finished, it is ready to run with **boot_linux.sh** or **boot_windows.bat**.
If you want to configure port and host of the server, it can be done by editing the values inside **config_server.py**:

<p align="center"><img src="https://i.ibb.co/FHzm6k6/server-Config.jpg)"/></p>

## Worker:
To run the worker, it takes a little more work, first keep in mind that you need [Python](https://www.python.org/downloads/) installed on the operating system, then check what operating system you have, in case you have Windows, go to the folder **install Windows** and in case you have Linux, go to the folder **install Linux**.
Then run the installers in the following order:

<p align="center"><img src="https://i.ibb.co/wNbg3TK/worker-Install.jpg)"/></p>

- First: **install miniconda**. Install miniconda, to generate a virtual environment and run Stable Diffusion.
- Second: **install miniconda dependencies**. Install miniconda dependencies, this installs everything needed to run Stable Diffusion on our device, such as CUDA, Pytorch, Torchvision, etc.
- Third: **install python dependencies**. Install the Python dependencies, to run Celery and connect to Redis.
- Fourth: **download Model**. Download the *ckpt* model to run the model, there are two methods to download it, from a Drive or from the HuggingFace page, it will be updated as versions are released. Most likely the Drive will be discontinued and only the one from the main page will be left. Remember to leave the model inside the **model** folder, in case of updating the model remember to change the name to **sd-v1-4.ckpt**, since that is the name of the model that it is looking for when you run Stable Diffusion.

In case you want to change the ip or port of the Redis to connect to, go into **/repositories/stable-diffusion/task.py** and change *ip:port* in **broker** and **backend**:

<p align="center"><img src="https://i.ibb.co/KNvW6Bk/worker-config.jpg)"/></p>

To execute, go to **boot_linux.sh** or **boot_windows.bat** depending on the operating system.

You can change settings when generating images by using the [following commands](https://github.com/CompVis/stable-diffusion#reference-sampling-script) and adding it in this part of the code, inside **system()**:

<p align="center"><img src="https://i.ibb.co/g7jFWhV/SD-config.jpg"/></p>.

Keep in mind that you risk bugs by making these changes.

# Instaladores (Spanish)
## Client:
El cliente no pide ningún requerimiento, solo hay que tener en cuenta, que todo corre sobre Python, por lo que se debe tener instalado [Python](https://www.python.org/downloads/) en el sistema operativo, recomendado versión 3.8 o superior. Ejecutar con **boot_linux.sh** o **boot_windows.bat** según sistema operativo, tener en cuenta de configurar el puerto y host del servidor en **client_config.py**:

<p align="center"><img src="https://i.ibb.co/RbjZY9F/Captura-de-pantalla-2022-12-08-122647.jpg)"/></p>

## Redis:
Para correr Redis **Docker** se debe tener instalado en el sistema operativo, los links de descarga se encuentran dentro del **install.txt**, una vez instalado Docker, en Windows se debe tener **Docker** ejecutando en segundo plano para ejecutar el Redis con **boot_windows.bat**, en linux con solo ejecutar **boot_linux.sh** listo. El redis corre sobre el puerto 6379:6379, si deseas cambiarlo, entra en el ejecutable y edita:

<p align="center"><img src="https://i.ibb.co/wgw4WQN/redis-Config.jpg)"/></p>

## Server:
Para correr el servidor se necesitan los requerimientos dentro del **requirements.txt**, tener en cuenta que para ejecutar el server se necesita [Python](https://www.python.org/downloads/) instalado en el sistema operativo, y con solo ejecutar **install_linux.sh** o **install_windows.bat** según tu sistema, se instalarán los requerimientos dentro de un entorno virtual, una vez finalizado, esta listo para ejecutar con **boot_linux.sh** o **boot_windows.bat**.
Si quieres configurar puerto y host del servidor, se puede editando los valores dentro de **config_server.py**:

<p align="center"><img src="https://i.ibb.co/FHzm6k6/server-Config.jpg)"/></p>

## Worker:
Para ejecutar el worker, lleva un poco mas de trabajo, tener primero en cuenta que necesitas [Python](https://www.python.org/downloads/) instalado en el sistema operativo, luego verifica que sistema operativo tienes, en caso de tener Windows, entra a la carpeta **install Windows** y en caso de tener Linux, entra a la carpeta **install Linux**.
Luego ir ejecutando los instaladores en el siguiente orden:

<p align="center"><img src="https://i.ibb.co/wNbg3TK/worker-Install.jpg)"/></p>

- Primero: **install miniconda**. Instalar miniconda, para generar un entorno virtual y ejecutar Stable Diffusion
- Segundo: **install miniconda dependencies**. Instalar las dependencias de miniconda, con esto se instala todo lo necesario para correr Stable Diffusion en nuestro dispositivo, como CUDA, Pytorch, Torchvision, etc.
- Tercero: **install python dependencies**. Instalar las dependencias de Python, para correr Celery y conectarse a Redis.
- Cuarto: **download Model**. Descargar el modelo *ckpt* para ejecutar el modelo, hay dos métodos de descargarlo, desde un Drive o desde la página principal de HuggingFace, se irá actualizando a medida que vayan saliendo versiones. Lo mas seguro que el Drive se descontinúe y se deje solo el de la página principal. Recordar dejar el modelo dentro de la carpeta **model**, en caso de actualizar el modelo recordar cambiar el nombre a **sd-v1-4.ckpt**, ya que ese es el nombre del modelo que busca al ejecutar Stable Diffusion.

En caso de querer cambiar la ip o puerto del Redis al cual conectarse, ir dentro de **/repositories/stable-diffusion/task.py** y cambiar *ip:port* en **broker** y **backend**:

<p align="center"><img src="https://i.ibb.co/KNvW6Bk/worker-config.jpg)"/></p>

Para ejecutar, ir a **boot_linux.sh** o **boot_windows.bat** según sistema operativo.

Se puede cambiar configuraciones al generar las imágenes utilizando los [siguientes comandos](https://github.com/CompVis/stable-diffusion#reference-sampling-script) y agregándolo en esta parte del código, dentro de **system()**:

<p  align="center"><img  src="https://i.ibb.co/g7jFWhV/SD-config.jpg"/></p>

Tener en cuenta que te arriesgas a fallos realizando estos cambios.