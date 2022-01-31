# reduced python as base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN pip install --upgrade pip

# set a directory for the app
WORKDIR /fastapi

# copy all the files to the container
COPY . /fastapi

# pip install dependencies
RUN pip install -r requirements.txt

EXPOSE 8000
# command that is run when container is started
CMD ["python", "main.py"]