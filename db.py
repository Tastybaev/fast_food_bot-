from pymongo import MongoClient

from settings import MONGO_DB, MONGO_LINK


client = MongoClient(MONGO_LINK)
db = client[MONGO_DB]

def get_or_create_user(db, effective_user, chat_id):
    user = db.users.find_one({
        'user_id': effective_user.id,
    })
    if not user:
        user = {
            'user_id': effective_user.id,
            'first_name': effective_user.first_name,
            'last_name': effective_user.last_name,
            'username': effective_user.username,
            'chat_id': chat_id
        }
        db.users.insert_one(user)
    return user


def get_menu(db):
    menu = db.menu.find({id: "1"})
    return menu
