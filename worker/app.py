import os

def run_celery():
    cores = os.cpu_count()
    print("Cores in use:", cores)
    os.system(f"celery -A tasks worker --loglevel=INFO -c{cores} -P eventlet")

if __name__ == "__main__":
    run_celery()