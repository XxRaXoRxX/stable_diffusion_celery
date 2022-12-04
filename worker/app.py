import os

def run_celery():
    cores = os.cpu_count()
    print("Cores in use:", cores)
    os.chdir(f"{os.getcwd()}/repositories/stable-diffusion")
    print(os.getcwd())
    #os.system(f"celery -A tasks worker --loglevel=INFO -c{cores} -P eventlet")
    os.system(f"celery -A tasks worker --loglevel=INFO -c{cores} -P eventlet")

if __name__ == "__main__":
    run_celery()