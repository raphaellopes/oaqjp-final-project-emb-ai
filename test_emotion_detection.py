import unittest
from  EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test1(self):
        # joy test case
        joy_test = emotion_detector('I am glad this happened')
        self.assertEqual(joy_test['dominant_emotion'], 'joy')

        # anger test case
        anger_test = emotion_detector('I am really mad about this')
        self.assertEqual(anger_test['dominant_emotion'], 'anger')

        # disgust test case
        disgust_test = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(disgust_score['dominant_emotion'], 'disgust')

        # sadness test case
        sadness_test = emotion_detector('I am so sad about this')
        self.assertEqual(sadness_test['dominant_emotion'], 'sadness')

        # fear test case
        fear_test = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(fear_test['dominant_emotion'], 'fear')

unittest.main()
