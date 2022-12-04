from celery import Celery
from os import path, system, listdir
import sys, base64, shutil

app = Celery('tasks', broker='redis://127.0.0.1:6379', backend='redis://127.0.0.1:6379')

@app.task
def GetImage(prompt):
    """Do stable diffusion image.

    args:
        - prompt: Text to transform in image."""

    system(f'python ./optimizedSD/optimized_txt2img.py --prompt "{prompt}" --ckpt ../../model/sd-v1-4.ckpt --H 512 --W 512 --n_samples 1')

    # Get Image
    folder = str(prompt).replace(' ', '_')
    folder = f'./outputs/txt2img-samples/{folder[:126]}/'

    for file in listdir(folder):
        with open(f"{folder}{file}", 'rb') as f:
            archive = base64.b64encode(f.read())
        shutil.rmtree(folder) # remove image folder
        return archive.decode()
    
    return None