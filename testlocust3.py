from locust import Locust, TaskSet, task

class stay(TaskSet):
    @task(3)
    def readBook(self):
        print ('I am reading a book.')

    @task(6)
    def listenMusic(self):
        print ('I am listening to music.')

    @task(1)
    def logOut(self):
        self.interrupt(reschedule=True)

class play(TaskSet):
    @task(2)
    def play(self):
        print ('I am playing a game.')

    @task(3)
    def gout(self):
        self.interrupt(reschedule=True)

class UserTask(TaskSet):
    tasks = {stay:1,play:2}

    @task(2)
    def leave(self):
        print ('I don not like this page.')

    @task(3)
    def go(self):
        print ('I just want to go.')

class User(Locust):
    task_set = UserTask