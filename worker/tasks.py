# Parte del Celery:
# La funcion_calculo podrá ser una de las siguientes:
# -raiz: calcula la raíz cuadrada del elemento.
# -pot: calcula la potencia del elemento elevado a si mismo.
# -log: calcula el logaritmo decimal de cada elemento.
from celery import Celery

app = Celery('tasks', broker='redis://127.0.0.1', backend='redis://127.0.0.1')

@app.task
def GetImage(prompt):
    """Do stable diffusion image.

    args:
        - prompt: Text to transform in image."""

    return prompt