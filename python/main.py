from crawler import DirectoryCrawler
from db_handler import DB_Handler
from user import User
from lesson import Lesson

if __name__ == "__main__":
    dc = DirectoryCrawler()
    db_handler = DB_Handler()
    logs = db_handler.read_local(dc.collector("*.json")[0])
    user_name = input("Enter user name:\t")
    user = User(user_name, logs)
    user_info = user.get_user()
    lesson = Lesson(user_info)
    lesson.create_problems()
