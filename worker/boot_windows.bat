:: Activate virtual environment.
call %UserProfile%\miniconda3\Scripts\activate.bat %UserProfile%\miniconda3\envs\stable-diffusion

:: Run Celery.
python3 app.py