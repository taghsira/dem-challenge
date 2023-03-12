#Section 2

##Problem Statement: 

Section 2 Details: ML Model Deployment  
Deploy (on a cloud provider [AWS, Azure, etc] or locally [docker, kubernetes, etc] ) an ML model such as (MNIST: https://paperswithcode.com/dataset/mnist, Fashion MNIST: https://github.com/zalandoresearch/fashion-mnist), as an API endpoint.  
 
Provide reproducible code with documentation for both deployment and usage. 

----
##Answer:
For this section I chose to locally deploy an MNIST model using docker with an API endpoint for usage. Keeping with the theme of using Python in section1, chose to use Flask 

###Assumptions:
- Model File already generated in any format supported by preferred frameworkvia TensorFlow, PyTorch, etc. 

###Instructions: 

Provided Docker is available on the system run: 
1. `docker build -t mnist-api .`
 - This will create a Docker image with the name mnist-api.

2. `docker run -p 8080:8080 mnist-api`
 - This will start the container and map port 8080 from the container to port 8080 on the machine this is run on. This will allow access to the API endpoint at `http://localhost:8080/predict`