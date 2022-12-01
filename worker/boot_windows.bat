:: Activate virtual environment.
call %UserProfile%\miniconda3\Scripts\activate.bat %UserProfile%\miniconda3\envs\ldm

:: Run Celery.
python3 app.py