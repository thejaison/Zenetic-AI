# this is for storing user memmory, it will be used to store the conversation history of each user

user_memmory = {}

def add_message(user_id, role, message):
    if user_id not in user_memmory:
        user_memmory[user_id] = []

    user_memmory[user_id].append(f"{role}: {message}")

def get_conversation(user_id):
    return "\n".join(user_memmory.get(user_id, [])) # this will return the conversation history of the user as a single string, with each message on a new line.

