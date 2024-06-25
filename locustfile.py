from locust import HttpUser, TaskSet, task, between


class UserBehavior(TaskSet):

    @task(1)
    def register_one_airquality(self):
        self.client.post(
            "/register_one",
            json={"timestamp": 1, "type_of_sensor": "AIRQUALITY", "read": 100.0},
        )

    @task(1)
    def register_many_airquality(self):
        self.client.post(
            "/register_many",
            json={
                "readings": [
                    {"timestamp": 1, "type_of_sensor": "AIRQUALITY", "read": 100.0},
                    {"timestamp": 2, "type_of_sensor": "AIRQUALITY", "read": 50.0},
                    {"timestamp": 3, "type_of_sensor": "AIRQUALITY", "read": -100.0},
                    {"timestamp": 4, "type_of_sensor": "AIRQUALITY", "read": 110.0},
                    {"timestamp": 5, "type_of_sensor": "AIRQUALITY", "read": -200.0},
                ]
            },
        )

    @task(1)
    def highest_accumulated_airquality(self):
        self.client.get("/highest_accumulated", params={"type_of_sensor": "AIRQUALITY"})

    @task(1)
    def register_one_uv(self):
        self.client.post(
            "/register_one",
            json={
                "timestamp": 1,
                "type_of_sensor": "ULTRAVIOLETRADIATION",
                "read": 5.0,
            },
        )

    @task(1)
    def register_many_uv(self):
        self.client.post(
            "/register_many",
            json={
                "readings": [
                    {
                        "timestamp": 1,
                        "type_of_sensor": "ULTRAVIOLETRADIATION",
                        "read": 5.0,
                    },
                    {
                        "timestamp": 2,
                        "type_of_sensor": "ULTRAVIOLETRADIATION",
                        "read": 3.0,
                    },
                    {
                        "timestamp": 3,
                        "type_of_sensor": "ULTRAVIOLETRADIATION",
                        "read": -1.0,
                    },
                    {
                        "timestamp": 4,
                        "type_of_sensor": "ULTRAVIOLETRADIATION",
                        "read": 7.0,
                    },
                    {
                        "timestamp": 5,
                        "type_of_sensor": "ULTRAVIOLETRADIATION",
                        "read": -2.0,
                    },
                ]
            },
        )

    @task(1)
    def highest_accumulated_uv(self):
        self.client.get(
            "/highest_accumulated", params={"type_of_sensor": "ULTRAVIOLETRADIATION"}
        )

    @task(1)
    def register_one_traffic(self):
        self.client.post(
            "/register_one",
            json={"timestamp": 1, "type_of_sensor": "TRAFFIC", "read": 200.0},
        )

    @task(1)
    def register_many_traffic(self):
        self.client.post(
            "/register_many",
            json={
                "readings": [
                    {"timestamp": 1, "type_of_sensor": "TRAFFIC", "read": 200.0},
                    {"timestamp": 2, "type_of_sensor": "TRAFFIC", "read": 150.0},
                    {"timestamp": 3, "type_of_sensor": "TRAFFIC", "read": -50.0},
                    {"timestamp": 4, "type_of_sensor": "TRAFFIC", "read": 250.0},
                    {"timestamp": 5, "type_of_sensor": "TRAFFIC", "read": -100.0},
                ]
            },
        )

    @task(1)
    def highest_accumulated_traffic(self):
        self.client.get("/highest_accumulated", params={"type_of_sensor": "TRAFFIC"})


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
