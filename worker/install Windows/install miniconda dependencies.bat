:: Tell the user if all is installed correctly.
echo Are you installed miniconda and create miniconda env?
choice /m Correct?
if %errorlevel% equ 1 goto INSTALL
if %errorlevel% equ 2 goto CANCEL

:INSTALL
call %UserProfile%\miniconda3\Scripts\activate.bat %UserProfile%\miniconda3\envs\ldm
cd ../repositories/stable-diffusion
conda env update --file environment.yaml
exit

:CANCEL
echo Installation cancelled.