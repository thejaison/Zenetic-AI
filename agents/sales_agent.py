from utils.sheets import save_to_sheet

user_state = {}

user_name = {}
user_age = {}
user_weight = {}

def handle_sales(user_id, message):
    if "plan" in message.lower() and user_state.get(user_id) is None:
        user_state[user_id] = "ask_name"
        return "Great! Let’s get started 💪\nWhat’s your name?"
    
    if user_state.get(user_id) == "ask_name":
        user_name[user_id] = message
        user_state[user_id] = "ask_age"
        return "Nice🍸! What’s your age?"
    
    if user_state.get(user_id) == "ask_age":
        try:
            age = int(message)
            user_age[user_id] = str(age)
            user_state[user_id] = "ask_weight"
            return "Got it! And what’s your current weight?"
        except ValueError:
            return "Please enter a valid age (number)."
    
    if user_state.get(user_id) == "ask_weight":
        try:
            weight = float(message)
            user_weight[user_id] = str(weight)
            user_state[user_id] = "ask_email"
            return "Perfect! What's your mail id?"
        except ValueError:
            return "Please enter a valid weight (number)."
    
    if user_state.get(user_id) == "ask_email":
        email = message
        if "@" not in email or "." not in email:
            return "Please enter a valid email address."

        save_to_sheet(
            user_name[user_id],
            user_age[user_id],
            user_weight[user_id],
            email
        )

        user_state[user_id] = None

        return "You're all set ✅ I’ll contact you soon!"
    return None