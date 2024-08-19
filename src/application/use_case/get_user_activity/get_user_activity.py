from src.domain.services.api_get import UrllibAPI


class GetUserActivityCommand:
    def __init__(self, username: str):
        self.username = username

    def execute(self):
        response = UrllibAPI().get(
            url=f"https://api.github.com/users/{self.username}/events",
        )
        return response
