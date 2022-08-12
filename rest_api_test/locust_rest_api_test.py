import json

from locust import HttpUser, constant, task


class ApiTest(HttpUser):
    # The wait_time method is an optional feature
    # used to make a simulated real user wait a specified time between task executions.
    # between(2,5) indicates that Locust will wait 2–5 seconds before proceeding with each task.

    # wait_time = constant(0.5)
    # wait_time = between(2, 5)

    def on_start(self):
        print("On Start Triggered")

    @task(1)
    def hello(self):
        self.client.post("/apis/v1/tracking/hello")

    # @task(2)
    # def track(self):
    #     self.client.post(
    #         "/apis/v1/tracking/track",  # url
    #         data=json.dumps(
    #             {  # payloads
    #                 "device_os": "Mac",
    #                 "browser": "Chrome",
    #                 "timestamp": "2022-08-09T15:32:21.131"
    #             }
    #         ),
    #         headers={
    #             'Content-type': 'application/json',
    #             'Accept': '*/*'
    #         }
    #     )

    def on_stop(self):
        print("On Stop Triggered")
