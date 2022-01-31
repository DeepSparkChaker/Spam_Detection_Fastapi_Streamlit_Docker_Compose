# reduced python as base image
FROM python:3.8-slim-buster 

# set a directory for the app
WORKDIR /streamlit

# copy all the files to the container
COPY . /streamlit

# pip install dependencies
RUN pip install -r requirements.txt

# expose port 8501 since streamlit runs on this port
EXPOSE 8501 

# command that is run when container is started
CMD ["streamlit", "run", "app.py"]
