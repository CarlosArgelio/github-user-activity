# GitHub Activity CLI
This is a simple command-line interface (CLI) tool that fetches and displays the recent activity of a specified GitHub user. The CLI leverages the GitHub API to retrieve the activity data and outputs it directly in the terminal.

## Features
- Accepts a GitHub username as a command-line argument.
- Fetches the recent activity of the specified GitHub user using the GitHub API.
- Displays the activity in a readable format in the terminal.
- Handles errors gracefully, such as invalid usernames or API failures.
- Built without the use of external libraries for data fetching.

## Usage

### Installation

1. Clone the repository:

```
git clone git@github.com:CarlosArgelio/github-user-activity.git
```

2. Make the script executable (optional):
```
chmod +x main.py
```

3. Install dependecit local
```
pip install -e .
```

## Running the CLI

To use the CLI, run the following command in your terminal:
```
github-activity <username>
```

### Example
```
github-activity CarlosArgelio
```

Output:
```
- Pushed 3 commits to kamranahmedse/developer-roadmap
- Opened a new issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/developer-roadmap
```

## Contributing
Contributions are welcome! If you have any ideas, feel free to fork the project and submit a pull request.

## License
This project is licensed under the MIT License.