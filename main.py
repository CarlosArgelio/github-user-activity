import sys
from presentation.command.command import GitHubActivityCommand


def main():
    username = sys.argv[1]
    GitHubActivityCommand(username).get_activity()


if __name__ == "__main__":
    main()
