echo creating model directory...
cd ..
mkdir model
cd model

echo Download model from drive (y) or huggingface (n) -Remember to paste downloaded archive inside model directory-?
choice /m Correct?
if %errorlevel% equ 1 goto Drive
if %errorlevel% equ 2 goto HF

:Drive
  start https://drive.google.com/file/d/1qYQJ6tuSO6QzFZQuMUBXOBP1nlozODG9/view?usp=share_link
:HF
  start https://huggingface.co/CompVis/stable-diffusion-v-1-4-original/resolve/main/sd-v1-4.ckpt