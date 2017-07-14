from locust import HttpLocust, TaskSet, task
import re

class WebsiteTasks(TaskSet):

    @task
    def coremail(self):
        response = self.client.post("/")
        print (dir(response))
        print ("response login code:",response.status_code)
        rscode = response.status_code
        if rscode == 200:
        	print (rscode)
        	self.client.get("/txguest",name="200")
        elif rscode == 403:
        	print (rscode)
        	self.client.get("/txguest",name="403")
        elif rscode == 502:
        	print (rscode)
        	self.client.get("/txguest",name="502")
        else:
        	print (rscode)
        	self.client.get("/",name="others")

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 3000
    max_wait = 3000