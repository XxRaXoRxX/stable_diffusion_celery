:: Run Redis Server.
docker rm stable-diffusion
docker run --name stable-diffusion -p 6379:6379 redis