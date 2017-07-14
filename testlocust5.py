from locust import HttpLocust, TaskSet, task

#Web 性能测试
class UserBehavior(TaskSet):

    def on_start(self):
    	"""on_start is called when a locust start before any task is scheduled"""
    	self.login()

    def login(self):
    	self.client.post("/login_action",{"username":"admin","password":"1234qwer"})

    @task(1)
    def event_manage(self):
        self.client.get("/event_manage/")

    @task(2)
    def guest_manage(self):
        self.client.get("/guest_manage/")

    @task(3)
    def search_phone(self):
        self.client.get("/search_phone/",params={"phone":'18500010001'})

#设置性能测试
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000