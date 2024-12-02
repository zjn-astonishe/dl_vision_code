docker run --gpus all -p 7000:9999 -it -v /home/zjn/Code/bert-sentiment/docker_data/:/root/docker_data/ -v /home/zjn/Code/bert-sentiment/:/root/code docker_tutorial --name vit /bin/bash -c "cd /root/code/ && source activate ml && python app.py"

docker run --gpus all -p 7000:9999 -it -v /home/zjn/Code/:/root/code -v /home/zjn/Document/DataSet/:/root/dataset  --name vit my_docker_py39_cuda118_cudnn8_torch222_tf214_ubuntu2204:latest /bin/bash 

docker build -f Dockerfile -t my_docker_py39_cuda118_cudnn8_torch222_tf214_ubuntu2204 .
