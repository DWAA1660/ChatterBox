from tests_django.base_case import ChatterBoxTestCase
from chatterbox.trainers import ChatterBoxCorpusTrainer


class ChatterBoxCorpusTrainingTestCase(ChatterBoxTestCase):
    """
    Test case for training with data from the ChatterBox Corpus.

    Note: This class has a mirror tests/training_tests/
    """

    def setUp(self):
        super().setUp()

        self.trainer = ChatterBoxCorpusTrainer(
            self.chatbot,
            show_training_progress=False
        )

    def tearDown(self):
        super().tearDown()
        self.chatbot.storage.drop()

    def test_train_with_english_greeting_corpus(self):
        self.trainer.train('chatterbox.corpus.english.greetings')

        results = list(self.chatbot.storage.filter(text='Hello'))

        self.assertGreater(len(results), 1)

    def test_train_with_english_greeting_corpus_tags(self):
        self.trainer.train('chatterbox.corpus.english.greetings')

        results = list(self.chatbot.storage.filter(text='Hello'))

        self.assertGreater(len(results), 1)
        statement = results[0]
        self.assertEqual(['greetings'], statement.get_tags())

    def test_train_with_multiple_corpora(self):
        self.trainer.train(
            'chatterbox.corpus.english.greetings',
            'chatterbox.corpus.english.conversations',
        )
        results = list(self.chatbot.storage.filter(text='Hello'))

        self.assertGreater(len(results), 1)

    def test_train_with_english_corpus(self):
        self.trainer.train('chatterbox.corpus.english')
        results = list(self.chatbot.storage.filter(text='Hello'))

        self.assertGreater(len(results), 1)
