import unittest

class GameStateTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_failed_example(self):
        self.assertEqual('foo'.upper(), 'foo')