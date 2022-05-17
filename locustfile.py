from locust import HttpUser, task, between #python module that imports packages

class AppUser(HttpUser):                   #class definition of users to be simulated which inherits HttpUser
    wait_time = between(1, 5)              #Simulated users wait time 

    @task                                  #micro thread
    def hello_page(self):                  #method that calls the api endpoint
        self.client.get("/")               #HTTP calls to be logged by locust
        

  
    