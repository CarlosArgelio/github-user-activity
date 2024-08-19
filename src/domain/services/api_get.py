import urllib.request
import urllib.error

import json


class UrllibAPI:
    def __init__(self) -> None:
        pass

    def get(self, **kwargs):
        URL = kwargs.get("url", None)

        try:
            with urllib.request.urlopen(URL) as response:
                content = response.read().decode("utf-8")
                json_data = json.loads(content)
                return json_data
        except urllib.error.HTTPError as e:
            print(f"HTTPError: {e.code} - {e.reason}")
        except urllib.error.URLError as e:
            print(f"URLError: {e.reason}")
        except Exception as e:
            print(f"Error inesperado: {e}")


class GithubEventList:
    def __init__(self, event) -> None:
        self.event = event
        self.repository = self.event["repo"]["name"]

    def get_create_event(self):
        split_name = self.repository.split(
            "/"
        )  # Get two values, first value is username account, seconds value is name repository

        return f"Created repository {split_name[1]} in {self.repository}"

    def get_push_event(self):
        count_commits = len(self.event["payload"]["commits"])
        return f"Pushed {count_commits} commits to {self.repository}"
