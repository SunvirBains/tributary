FROM python:3.11
COPY ./requirements.txt . 

RUN pip install -r requirements.txt 

COPY ./entrypoint.py .
CMD exec gunicorn entrypoint:app

# RUN executes during the image building process
#The cmd is used to set default command that will be excuted when docker container start 