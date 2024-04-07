from pymongo import MongoClient
from config import mongo
from pymongo.collection import ReturnDocument

# Initialize MongoDB connection
client = MongoClient(mongo)
db = client['main']
users = db['users']
groups = db['groups']

def already_db(user_id):
    """Check if a user exists in the database."""
    return users.find_one({"user_id": str(user_id)}) is not None

def already_dbg(chat_id):
    """Check if a group exists in the database."""
    return groups.find_one({"chat_id": str(chat_id)}) is not None

def add_user(user_id):
    """Add a new user to the database."""
    if already_db(user_id):
        return "User already exists"
    result = users.insert_one({"user_id": str(user_id)})
    return result.inserted_id

def remove_user(user_id):
    """Remove a user from the database."""
    if not already_db(user_id):
        return "User not found"
    result = users.delete_one({"user_id": str(user_id)})
    return result.deleted_count

def add_group(chat_id):
    """Add a new group to the database."""
    if already_dbg(chat_id):
        return "Group already exists"
    result = groups.insert_one({"chat_id": str(chat_id)})
    return result.inserted_id

def remove_group(chat_id):
    """Remove a group from the database."""
    if not already_dbg(chat_id):
        return "Group not found"
    result = groups.delete_one({"chat_id": str(chat_id)})
    return result.deleted_count

def all_users():
    """Count all users in the database."""
    return users.count_documents({})

def all_groups():
    """Count all groups in the database."""
    return groups.count_documents({})
