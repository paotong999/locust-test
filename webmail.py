from locust import HttpLocust, TaskSet, task
import re

class WebsiteTasks(TaskSet):
    def on_start(self):
        response = self.client.get("/coremail")


    @task
    def coremail(self):
        response = self.client.post("/coremail/login.jsp",{
            "uid":"cunzheng@cz.icoremail.net",
            "password":"CZadmin@123"
        })
        print (dir(response))
        print ("response login code:",response.status_code)
        print ("response headers:",response.headers)
        print (response.headers.keys())
        print ("response coremail code:",response.status_code)
        print (response.headers.get('Set-Cookie','none'))
        sid_tmp = re.compile(r'Coremail.sid=([\w]+);').search(response.headers.get('Set-Cookie','none'))
        if sid_tmp is not None:
            sid = sid_tmp.groups()[0]
        self.client.get("/coremail/XT5/index.jsp?sid=%s#mail.welcome" % sid, name="/coremail/XT5/index.jsp?sid")
        print (sid)

    @task
    def about(self):
        self.client.get("/coremail/help")

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 3000
    max_wait = 3000