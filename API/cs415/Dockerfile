# A Dockerfile is a text document that contains all the commands a user 
# could call on the command line to assemble an image.

# This is my operating system
# FROM ubuntu:22.04 

# This is copying all the files from my project into my image
# In a directory called /app
# COPY . /app

# RUN python3 manage.py runserver
# CMD echo "I am a container!"

FROM ubuntu
RUN apt update -y && \
    apt-get install python3-pip python3-dev default-libmysqlclient-dev build-essential apache2 libapache2-mod-wsgi-py3 -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
COPY . /cs415/
WORKDIR /cs415
RUN pip install -r requirements.txt
COPY 000-default.conf /etc/apache2/sites-available/
EXPOSE 80