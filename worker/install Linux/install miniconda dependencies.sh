read -p "Are you installed miniconda and create miniconda env? [Y/n] "
response=${response,,}  # convert to lowercase
case $response in
    y|ye|yes)
        echo "Installing..."
        source $HOME/miniconda3/bin/activate
        conda activate ldm
        cd ../repositories/stable-diffusion
        conda env update --file environment.yaml
    ;;
    *)
      echo "installation cancelled."
    ;;
esac