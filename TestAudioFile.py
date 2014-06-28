import unittest

from AudioFile import AudioFile


class TestAudioFile(unittest.TestCase):
    #

    def test_audio(self):
        audio = AudioFile('./test_collection/2/Test.mp3', 'Test.mp3',
                          './test_collection')
        self.assertEqual(
            audio.relpath,
            '2/Test.mp3')
        self.assertEqual(audio.size, 4594747)
        self.assertEqual(audio.length, 287.13795918367344)
        self.assertEqual(audio.name, '2')
        self.assertEqual(audio.album, 'Cool')
        self.assertEqual(audio.genre, 'Electronic')
        self.assertEqual(audio.year, '2014')

if __name__ == '__main__':
    unittest.main()
