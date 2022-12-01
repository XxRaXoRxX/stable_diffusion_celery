echo Downloading miniconda.
powershell -command "Invoke-WebRequest -Uri https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -OutFile ~\miniconda.exe"

echo Installing miniconda.
start /B /WAIT %UserProfile%\miniconda.exe /InstallationType=JustMe /AddToPath=0 /RegisterPython=0 /S /D=%UserProfile%\miniconda3

echo Deleting installer.
del %UserProfile%\miniconda.exe

echo Running conda and creating environment
call %UserProfile%\miniconda3\Scripts\activate.bat
conda create --name ldm

::echo "Updating miniconda"
::call %UserProfile%\miniconda3\Scripts\activate.bat
::conda update -n base -c defaults conda