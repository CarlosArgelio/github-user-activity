from src.application.use_case.get_user_activity.get_user_activity import (  # type: ignore
    GetUserActivityCommand,
)


class ManageCommand:

    def execute(self, username: str):
        print(GetUserActivityCommand(username).execute())


#         print(username)
#         print(
#             """
# Output:
# - Pushed 3 commits to kamranahmedse/developer-roadmap
# - Opened a new issue in kamranahmedse/developer-roadmap
# - Starred kamranahmedse/developer-roadmap
#         """
#         )
