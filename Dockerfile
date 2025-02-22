FROM python:3.7-slim
ARG VERSION
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8
ENV TZ=Asia/Shanghai

RUN apt-get update -y \
		&& apt install -y gettext gcc make cmake libmariadb-dev curl libc6-dev unzip cron  openjdk-11-jdk fonts-wqy-microhei vim
#     htop sysstat net-tools iproute2 procps lsof
    
RUN curl -L https://github.com/Endava/cats/releases/download/cats-7.0.1/cats-linux -o  /usr/local/bin/cats \
	&& chmod +x /usr/local/bin/cats \
	&& ln -s /usr/local/bin/cats /usr/bin/cats


COPY requirements-prod.txt /opt/dongtai/webapi/requirements.txt
RUN pip3 install -r /opt/dongtai/webapi/requirements.txt

# debug performance ...
COPY . /opt/dongtai/webapi
WORKDIR /opt/dongtai/webapi

RUN mkdir -p /tmp/iast_cache/package && mv /opt/dongtai/webapi/*.jar /tmp/iast_cache/package/ || true && mv /opt/dongtai/webapi/*.tar.gz /tmp/ || true 
ENTRYPOINT ["/bin/bash","/opt/dongtai/webapi/docker/entrypoint.sh"]
