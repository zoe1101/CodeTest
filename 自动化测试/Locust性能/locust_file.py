from locust import HttpUser, TaskSet, task, between


class UserBehavior(TaskSet):

    def on_start(self):
        """
        Called when a User starts executing this TaskSet
        """
        pass

    def on_stop(self):
        """
        Called when a User stops executing this TaskSet. E.g. when TaskSet.interrupt() is called
        or when the User is killed
        """
        pass

    @task(1)
    def baidu_homepage(self):
        self.client.get("/")

    @task(2)
    def baidu_search(self):

        with self.client.get("/s?wd=chatgpt", catch_response=True) as response:

            if response.status_code != 200:
                response.success()
            else:
                response.failure("请求失败")

            if response.json()["param1"] != "xx":
                response.failure("请求失败，No data")

            # 支持断言检查 assert response.json()['param1'] == 100,"数据返回错误"

        # Post请求例子 res = self.client.post("/login", json={"username": "foo", "password": "bar"})


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    host = "https://www.baidu.com"

    # 等待响应时间在3-7s内，超时处理策略
    wait_time = between(3, 7)
