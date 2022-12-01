from celery import Celery
from os import path, system
import sys

app = Celery('tasks', broker='redis://127.0.0.1:6379', backend='redis://127.0.0.1:6379')

@app.task
def GetImage(prompt):
    """Do stable diffusion image.

    args:
        - prompt: Text to transform in image."""

    #system(f"./repositories/stable-diffusion/scripts/txt2img.py --prompt {prompt} --plms --outdir ./images/")

    return prompt