# Parte del Celery:
# La funcion_calculo podrá ser una de las siguientes:
# -raiz: calcula la raíz cuadrada del elemento.
# -pot: calcula la potencia del elemento elevado a si mismo.
# -log: calcula el logaritmo decimal de cada elemento.
from celery import Celery

app = Celery('tasks', broker='redis://127.0.0.1', backend='redis://127.0.0.1')

@app.task
def Root(value):
    """Calcula la raíz cuadrada del elemento.

    args:
            -value: Valor a realizar el calculo."""

    newMatrix = []

    for v in value:
        newMatrix.append(math.sqrt(v))

    return newMatrix

@app.task
def Pot(value):
    """Calcula la potencia del elemento elevado a si mismo.

    args:
            -value: Valor a realizar el calculo."""

    newMatrix = []

    for v in value:
        newMatrix.append(math.pow(v, v))

    return newMatrix

@app.task
def Log(value):
    """Calcula el logaritmo decimal de cada elemento.

    args:
            -value: Valor a realizar el calculo."""

    newMatrix = []

    for v in value:
        newMatrix.append(math.log(v))

    return newMatrix

if __name__ == "__main__":
    app.start()

# Para ejecutar Celery:
# celery -A tasks worker --loglevel=INFO -c4