import json

class DB_Handler():
    """
    Handle reading and writing from / to local and remote databases
    """

    def read_local(self, file):
        """Read data from a local data source

        Args:
            file (json): doc with records stored locally
        """
        with open(file, "r+") as records:
            logs = json.load(records)
            return(logs)

