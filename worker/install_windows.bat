:: Download virtualenv
pip3 install virtualenv

:: Get stable-diffusion git branch
cd repositories
git clone "https://github.com/CompVis/stable-diffusion"
cd ..

:: Create virtual environment
python3 -m venv env
call env\Scripts\activate.bat

:: Install requirements
pip3 install -r ./requirements.txt