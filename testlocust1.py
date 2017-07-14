from locust import HttpLocust, TaskSet, task

#定义用户行为
class UserBehavior(TaskSet):

    @task(1)
    def baidu(self):
        self.client.get("/")

#设置性能测试
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000