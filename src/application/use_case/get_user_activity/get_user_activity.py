from src.domain.services.api_get import UrllibAPI, GithubEventList


class GetUserActivityCommand:
    def __init__(self, username: str):
        self.username = username

    def execute(self):
        output = []

        response = UrllibAPI().get(
            url=f"https://api.github.com/users/{self.username}/events",
        )

        for event in response:

            manage_events = GithubEventList(event)

            if event["type"] == "CreateEvent":
                output.append(manage_events.get_create_event())
            elif event["type"] == "PushEvent":
                output.append(manage_events.get_push_event())
            else:
                pass

        return output
