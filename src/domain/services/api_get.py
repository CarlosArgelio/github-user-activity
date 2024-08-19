import urllib.request
import urllib.error


class UrllibAPI:
    def __init__(self) -> None:
        pass

    def get(self, **kwargs):
        URL = kwargs.get("url", None)

        try:
            with urllib.request.urlopen(URL) as response:
                content = response.read().decode("utf-8")
                print(content)
        except urllib.error.HTTPError as e:
            print(f"HTTPError: {e.code} - {e.reason}")
        except urllib.error.URLError as e:
            print(f"URLError: {e.reason}")
        except Exception as e:
            print(f"Error inesperado: {e}")
