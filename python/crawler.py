from pathlib import Path

class DirectoryCrawler():
    """Look for the specified file(s)"""

    def collector(self, file_extension):
        """Crawl through the folder and subfolders.
        Return a list of all files of the provided extension
        args: file_name, file_extension: eg *.txt, data.csv"""

        files = list(Path.cwd().rglob(file_extension))
        return files