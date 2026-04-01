from agents.chat_agent import generate_reply
# from agents.sales_agent import analyze_conversation
from utils.memory import add_message, get_conversation

GOOGLE_FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSfTHtFKWE45_8hsNyB1eXcbVEXx3hP3FEW46wle622TxIRuJA/viewform?usp=publish-editor"

def handle_message(user_id, message):
    add_message(user_id, "User", message)

    conversation = get_conversation(user_id)

    reply = generate_reply(message, conversation)

    add_message(user_id, "AI", reply)

    return reply

if __name__ == "__main__":
    user_id = "test_user"

    while True:
        msg = input("User: ")

        if msg.lower() == "exit":
            print("Exiting...")
            break

        if not msg.strip():
            continue

        res = handle_message(user_id, msg)
        print("AI:", res)