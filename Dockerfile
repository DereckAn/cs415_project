# A Dockerfile is a text document that contains all the commands a user 
# could call on the command line to assemble an image.

# This is my operating system
FROM ubuntu:22.04 

# This is copying all the files from my project into my image
# In a directory called /app
COPY . /app

# RUN python3 manage.py runserver
CMD echo "I am a container!"