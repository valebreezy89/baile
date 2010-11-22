import unittest
from baile.av.encoder import Encoder, EncoderException, EncoderListener
class EncoderTest(unittest.TestCase):
    def setUp(self):
        #this statement should go clear if mencoder dependency is satisfied
        self.encoder = Encoder()
        self.listener = TestListsner()
        self.encoder.addListener(self.listener)
    def testSimpleOnePass(self):
        self.listener.reset()
        settings = dict(vcodec="copy", acodec="pcm") #copy video as is, encode audio to PCM
        self.encoder.encode("../test_data/small.ogg","../test_data/results/small.ogg", settings)
        self.assertTrue(self.listener.isStarted)
        self.assertTrue(self.listener.isFinished)
        self.assertTrue(len(self.listener.progresses) > 0)
'''
Test encoder listener for counting events.
'''
class TestListsner(EncoderListener):
    def __init__(self):
        self.reset()
    def reset(self):
        self.progresses = []
        self.stages = []
        self.isStarted = False
        self.isInterrupted = False
        self.isFinished = False
    def progress(self, progress):
        self.progresses.append(progress)
    def stage(self, stage):
        self.stages.append(stage)
    def started(self):
        self.isStarted = True
    def interrupted(self, reason):
        self.isInterrupted = True
    def finished(self):
        self.isFinished = True

        
