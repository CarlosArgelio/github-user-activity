from src.application.use_case.get_user_activity.get_user_activity import (  # type: ignore
    GetUserActivityCommand,
)


class ManageCommand:

    def execute(self, username: str):
        response = GetUserActivityCommand(username).execute()
        for event in response:
            print(f"- {event}")
