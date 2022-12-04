read -p "Are you installed miniconda dependencies? [Y/n] "
response=${response,,}  # convert to lowercase
case $response in
    y|ye|yes)
        echo "Installing..."
        source $HOME/miniconda3/bin/activate
        conda activate ldm
        cd ..
        pip install -r ./requirements.txt
        cd ./repositories/stable-diffusion
        pip install transformers==4.19.2 diffusers invisible-watermark
        conda install pytorch torchvision -c pytorch
    ;;
    *)
      echo "installation cancelled."
    ;;
esac