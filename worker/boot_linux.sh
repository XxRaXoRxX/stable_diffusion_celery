# Avtivate virtual environment.
source bin/activate

# Run Celery.
n = int(input("How much cores do you whant to use?: "))
celery -A tasks worker --loglevel=INFO -c n