# FROM ubuntu:18.04
# FROM nvidia/cuda:10.2-cudnn7-runtime-ubuntu18.04
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN apt update \
    && apt install -y htop python3-dev wget libgl1 libglib2.0-0

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir root/.conda \
    && sh Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh

RUN conda create -y -n ml python=3.9

# COPY . src/
# RUN /bin/bash -c "cd src \
#     && source activate ml \
#     && pip install -r requirements.txt"

RUN /bin/bash -c "source activate ml\
    && pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu118 \
    && pip install tensorflow==2.14.0 \
    && pip install tensorflow-probability==0.22.1\
    && pip install opencv-python\
    && pip install -U scikit-learn\
    && pip install patchify \
    && conda install -c nvidia cuda-nvcc"
