from chatterbox import ChatBot


# Create a new instance of a ChatBot
bot = ChatBot(
    'Exact Response Example Bot',
    storage_adapter='chatterbox.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbox.logic.BestMatch'
        },
        {
            'import_path': 'chatterbox.logic.SpecificResponseAdapter',
            'input_text': 'Help me!',
            'output_text': 'Ok, here is a link: http://chatterbox.rtfd.org'
        }
    ]
)

# Get a response given the specific input
response = bot.get_response('Help me!')
print(response)
