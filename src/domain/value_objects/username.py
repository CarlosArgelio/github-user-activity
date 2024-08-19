class Username:
    value: str

    def __init__(self, username) -> None:
        self.value = username
        self.validate()

    def is_string(self) -> bool:
        return isinstance(self.value, str)

    def is_not_empty_or_whitespace(self) -> bool:
        return bool(self.value.strip())

    def validate(selg):
        if not selg.is_string():
            raise ValueError("Username must be a string")
        elif not selg.is_not_empty_or_whitespace():
            raise ValueError("Username cannot be empty or whitespace")
