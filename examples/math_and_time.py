from chatterbox import ChatBot


bot = ChatBot(
    'Math & Time Bot',
    logic_adapters=[
        'chatterbox.logic.MathematicalEvaluation',
        'chatterbox.logic.TimeLogicAdapter'
    ]
)

# Print an example of getting one math based response
response = bot.get_response('What is 4 + 9?')
print(response)

# Print an example of getting one time based response
response = bot.get_response('What time is it?')
print(response)
