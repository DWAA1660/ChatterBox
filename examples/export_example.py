from chatterbox import ChatBot
from chatterbox.trainers import ChatterBoxCorpusTrainer

'''
This is an example showing how to create an export file from
an existing chat bot that can then be used to train other bots.
'''

chatbot = ChatBot('Export Example Bot')

# First, lets train our bot with some data
trainer = ChatterBoxCorpusTrainer(chatbot)

trainer.train('chatterbox.corpus.english')

# Now we can export the data to a file
trainer.export_for_training('./my_export.json')
