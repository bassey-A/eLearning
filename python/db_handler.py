import json
import user


class DB_Handler:
    """
    Handle reading and writing from / to local and remote databases
    """

    def read_local(self, file: str) -> dict[str, dict[str, int | str]] | None:
        """Read data from a local data source

        Args:
            file (json): doc with records stored locally
        """
        try:
            with open(file, "r+") as records:
                logs = json.load(records)
            return logs
        except IOError as e:
            print(f"Error opening {file}: {e}")
        except Exception as e:
            print(f"Error opening {file}: {e}")

    def write_local(self, file: str, user: user.User) -> None:
        """Update the local DB

        Args:
            file (path): file to write
        """

        dump: dict[str, dict[str, int | str]] | None = self.read_local(file)
        if dump is not None:
            rec: dict[str, dict[str, int | str]] = {
                user.get_name(): {
                    "days_active": user.streak,
                    "last_date": user.last_date,
                    "name": user.get_name(),
                }
            }
            dump.update(rec)
            print("updated")

            with open(file, "w") as f:
                json.dump(dump, f, indent=4)

        else:
            print("closed")
