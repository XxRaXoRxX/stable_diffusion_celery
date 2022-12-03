echo "Downloading miniconda."
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh

echo "Installing miniconda."
bash ~/miniconda.sh -b -p

echo "Deleting installer."
rm ~/miniconda.sh

echo "Running conda and creating environment"
source $HOME/miniconda3/bin/activate
conda create --name ldm

#echo "Updating miniconda"
#call %UserProfile%\miniconda3\Scripts\activate.bat
#conda update -n base -c defaults conda