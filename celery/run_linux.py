import os

if __name__ == '__main__':
    cores = os.cpu_count()
    print("Cores in use: ", cores)
    os.system(f"celery -A tasks worker --loglevel=INFO -c{cores}")