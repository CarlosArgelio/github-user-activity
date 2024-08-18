import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: github-activity {string}")
        sys.exit()

    input = sys.argv[1]
    print(f"Hola mundo, {input}")


if __name__ == "__main__":
    main()
