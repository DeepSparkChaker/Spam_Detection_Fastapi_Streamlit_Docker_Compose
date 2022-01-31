# Serving ML Models as Microservices - Streamlit, FastAPI, and Docker

This repo contains code for a small webapp to predict if we have a spam messages .

 The application consists of a frontend and a backend part and is used to demonstrate how to serve ML models as microservices through an API.
 The frontend is built with Streamlit and used to acquire messages. 
 
 The backend is built with the FastAPI framework and consists of  endpoints: `/^predict_spam/`  to get the message label andprobability in percent as a response from the API. 

# How to run the Application

Both parts are containerized with Docker and combined via Docker-Compose.

 To run the app, simply clone the repo (or copy the docker-compose.yml) and run `docker-compose up` from the terminal. 
 
In this example, we serve an spam  model using FastAPI for the backend service and streamlit for the frontend service. 
docker-compose orchestrates the two services and allows communication between them.

To run the example in a machine running Docker and docker-compose, run:


		docker-compose build
		docker-compose up


To visit the FastAPI documentation of the resulting service, visit http://localhost:8000 with a web browser.
To visit the streamlit UI, visit http://localhost:8501.
http://192.168.99.100:8501/

Logs can be inspected via:

docker-compose logs

If you have made some changes in your yml file configuration, you first need to stop your containers by:

"docker-compose down" 

Then to run again your application, use this command:

"docker-compose up -d" , "docker-compose up -d --build"



 
links : 
https://tlary.github.io/post/fastapi/

https://github.com/tlary/fastapi_titanic/tree/main/app

https://github.com/davidefiocco/streamlit-fastapi-model-serving

https://github.com/RihabFekii/streamlit-app/blob/master/docker-compose.yml

https://testdriven.io/blog/fastapi-streamlit/
# Deploy streamlit+ fast api + docker composer to heroku : 

https://github.com/davidefiocco/streamlit-fastapi-model-serving

https://davidefiocco.github.io/streamlit-fastapi-ml-serving/

https://testdriven.io/blog/fastapi-streamlit/

https://pythonrepo.com/repo/davidefiocco-streamlit-fastapi-model-serving

https://github.com/davidefiocco/streamlit-fastapi-model-serving


http://102.157.162.189:8501