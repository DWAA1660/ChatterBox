from chatterbox import ChatBot


# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbox.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbox.logic.MathematicalEvaluation',
        'chatterbox.logic.TimeLogicAdapter',
        'chatterbox.logic.BestMatch'
    ],
    database_uri='sqlite:///database.sqlite3'
)

print('Type something to begin...')

# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input()

        bot_response = bot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
