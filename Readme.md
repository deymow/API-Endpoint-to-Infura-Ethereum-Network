## Infura Test 
This web application was built using python with Flask framework. The entrypoint of the application is the app.py file. A dockerfile has been included to package all the necessary dependencies of the application into a container. This project also contains a docker-compose file which is used to run the docker container. A load testing framework, locust was used to perform load testing on application.

### Requirements
- Docker
- Docker Compose

## Steps
- Clone repository
- Luanch terminal and change directory into repository
- Run command `docker-compose up -d` to launch container in detached mode
- Goto `http://localhost:5000` to access application
- Run commamd `docker-compose down -rmi all` to shutdown application and remove related resources

## How to run Load Test using locust
Please ensure that you have python installed on your local system
- Install necessary dependencies `pip install -r requirements.txt`
- Run locust -f locustfile.py
- Run http://localhost:8089 (default locust path) to access test application
- On the web, enter the number of users that will access the app
- The spawn rate can be set to the default which is 1 
- Enter the address the python app to be tested is running on http://localhost:5000
- Click on Start swarming to simulate multiple users as shown in the screenshot below
