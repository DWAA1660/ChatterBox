from chatterbox import ChatBot
from chatterbox.trainers import ChatterBoxCorpusTrainer
import logging


'''
This is an example showing how to train a chat bot using the
ChatterBox Corpus of conversation dialog.
'''

# Enable info level logging
logging.basicConfig(level=logging.INFO)

chatbot = ChatBot('Example Bot')

# Start by training our bot with the ChatterBox corpus data
trainer = ChatterBoxCorpusTrainer(chatbot)

trainer.train(
    'chatterbox.corpus.english'
)

# Now let's get a response to a greeting
response = chatbot.get_response('How are you doing today?')
print(response)
