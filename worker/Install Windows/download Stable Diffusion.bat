::echo "Get stable-diffusion git branch"
cd ../repositories
:: More than 10GB VRam videocard
::git clone https://github.com/CompVis/stable-diffusion 
:: Less than 10GB VRam videocard
git clone https://github.com/basujindal/stable-diffusion
cd ..
copy tasks.py .\repositories\stable-diffusion