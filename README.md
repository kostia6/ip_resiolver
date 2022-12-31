To build and run docker image:

docker build -t myimage .

docker run -d --name mycontainer -p 8000:8000 myimage

Test the api:

http://localhost:8000/ip-service/8.8.8.8

Run locally:

http://localhost:8001/ip-service/8.8.8.8

