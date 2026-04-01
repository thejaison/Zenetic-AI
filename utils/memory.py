# this is for storing user memory, it will be used to store the conversation history of each user

user_memory = {}

def add_message(user_id, role, message):
    if user_id not in user_memory:
        user_memory[user_id] = []

    user_memory[user_id].append(f"{role}: {message}")

def get_conversation(user_id):
    return "\n".join(user_memory.get(user_id, [])) # this will return the conversation history of the user as a single string, with each message on a new line.

