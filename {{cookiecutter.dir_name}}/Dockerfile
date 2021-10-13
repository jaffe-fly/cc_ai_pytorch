# Start FROM Nvidia PyTorch image https://ngc.nvidia.com/catalog/containers/nvidia:pytorch
FROM pytorch/pytorch:1.8.1-cuda11.1-cudnn8-devel
#FROM pytorch/pytorch:1.8.1-cuda11.1-cudnn8-runtime

# Install linux packages
RUN apt update && apt install -y zip git libsm6 libxext6 libxrender-dev unzip llvm-dev vim libgl1-mesa-glx libglib2.0-dev g++

# time zone set
WORKDIR /usr/share
ADD zoneinfo ./zoneinfo
RUN  ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo "Asia/Shanghai" > /etc/timezone

# models
WORKDIR /opt
ADD requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install --no-cache -i https://mirrors.cloud.tencent.com/pypi/simple -r requirements.txt

ADD conf ./conf
ADD pretrained ./pretrained
ADD server.py .
ADD train.py .
ADD tests/flasktest.py .
ADD train.sh .
ADD server.sh .
