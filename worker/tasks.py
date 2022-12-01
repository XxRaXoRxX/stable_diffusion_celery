from celery import Celery
from os import path, system
import sys

app = Celery('tasks', broker='redis://127.0.0.1:6379', backend='redis://127.0.0.1:6379')

@app.task
def GetImage(prompt):
    """Do stable diffusion image.

    args:
        - prompt: Text to transform in image."""

    system(f'python ./optimizedSD/optimized_txt2img.py --prompt "{prompt}" --ckpt ../../model/model.ckpt --H 512 --W 512 --n_samples 1')

    return prompt