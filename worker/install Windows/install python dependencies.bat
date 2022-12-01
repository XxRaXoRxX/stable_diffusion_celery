:: Tell the user if all is installed correctly.
echo Are you installed miniconda dependencies?
choice /m Correct?
if %errorlevel% equ 1 goto INSTALL
if %errorlevel% equ 2 goto CANCEL

:INSTALL
call %UserProfile%\miniconda3\Scripts\activate.bat %UserProfile%\miniconda3\envs\ldm
cd ..
pip install -r ./requirements.txt
cd ./repositories/stable-diffusion
pip install transformers==4.19.2 diffusers invisible-watermark
conda install pytorch torchvision -c pytorch
exit

:CANCEL
echo Installation cancelled.