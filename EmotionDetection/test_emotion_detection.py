import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection (unittest.TestCase):
    def test_emotion_detector(self):
        self.assertEqual(emotion_detector('I am glad this happened'), 'Joy')

if __name__ = '__main__':
    unittest.main()