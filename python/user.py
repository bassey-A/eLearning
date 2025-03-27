import json

class User():
    """
    Manage users of the system.
    Methods:
        create_user, delete_user, get_user, update_user
    """

    def __init__(self, name, logs):
        """name: string, subjects: list, streak: integer"""
        self.name = name
        self.logs = logs
        self.streak = 0

    def create_user(self):
        """Create new user."""
        pass

    def delete_user(self):
        """Delete specified user."""
        pass

    def get_user(self):
        """Get specified user.
        Args: 
            file (string): username to find.
            logs (dictionary): entries to search.
        """
        if self.name in self.logs["users"]:
            return self.logs["users"][self.name]

        

    def update_user():
        """Update remote records for specified user."""
        pass

# 1. Get user details
# 2. Check db for user
# 3. Get user info, or prompt to create user
### Figure out how to check for user on db: pull down or query
### use algolia for searches on firestore
### use firebase realtime database
### create cloud firestore and compare both