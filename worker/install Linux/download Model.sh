echo "creating model directory..."
cd ..
mkdir model
cd ./model

read -p "Download model from drive (y) or huggingface (n) -Remember to paste downloaded archive inside model directory-"
response=${response,,}  # convert to lowercase
case $response in
    y|ye|yes)
      echo "Downloading from drive"
      xdg-open https://drive.google.com/file/d/1qYQJ6tuSO6QzFZQuMUBXOBP1nlozODG9/view?usp=share_link
    ;;
    n|no)
      echo "Downloading from huggingface"
      xdg-open https://huggingface.co/CompVis/stable-diffusion-v-1-4-original/resolve/main/sd-v1-4.ckpt 
    ;;
    *)
      echo "installation cancelled."
    ;;
esac