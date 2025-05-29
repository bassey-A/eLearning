from datetime import date


class User:
    """
    Manage users of the system.
    Methods:
        delete_user, get_name, update_user
    """

    def __init__(
        self, name: str, last_date: str = date.today().isoformat(), streak: int = 0
    ) -> None:
        """name: string, last_date: date"""
        self.name = name.casefold()
        self.last_date = last_date
        self.streak = streak

    def __repr__(self) -> str:
        return f"{self.name}, {self.last_date}, {self.streak}"

    def __str__(self) -> str:
        return f"Hi {self.name.capitalize()}. \nYour last activity was on {self.last_date}. \nCurrent streak: {self.streak}"

    def __call__(self) -> None:
        print(f"{self.name} created @ {date.today()}")

    def delete_user(self) -> None:
        """Delete specified user."""
        pass

    def get_name(self) -> str:
        """Return name of the user"""
        return self.name


# 2. Check db for user
# 3. Get user info, or prompt to create user

### use algolia for searches on firestore
### use firebase realtime database
### create cloud firestore and compare both
