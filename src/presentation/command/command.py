from src.infraestructure.command.command import ManageCommand


class GitHubActivityCommand:
    def __init__(self, username: str):
        self.username = username

    def get_activity(self):
        ManageCommand().execute(self.username)
