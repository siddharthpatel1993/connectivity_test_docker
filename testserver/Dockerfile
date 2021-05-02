FROM ubuntu
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python2 telnet netcat vim
RUN mkdir -p home/configuration_and_log
COPY configuration_and_log/configuration_url_service.txt /home/configuration_and_log/configuration_url_service.txt
COPY configuration_and_log/configuration_manual_change.txt /home/configuration_and_log/configuration_manual_change.txt
COPY connectivity_test.py /home/connectivity_test.py
WORKDIR /home
