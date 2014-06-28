import unittest

from MusicCollection import MusicCollection


class TestMusicCollection(unittest.TestCase):
    #

    def test_all(self):
        mc = MusicCollection("./test_collection/", flac=True, ogg=True)
        self.assertEqual(len(mc.audio_files), 9)

    def test_flac(self):
        mc = MusicCollection("./test_collection/", flac=True)
        self.assertEqual(len(mc.audio_files), 8)

    def test_ogg(self):
        mc = MusicCollection("./test_collection/", ogg=True)
        self.assertEqual(len(mc.audio_files), 8)

    def test_mp3(self):
        mc = MusicCollection("./test_collection/")
        self.assertEqual(len(mc.audio_files), 7)

    def test_search_by_minutes(self):
        mc = MusicCollection("./test_collection/", flac=True, ogg=True)
        self.assertEqual(mc.search_by_length_in_minutes('< 4'),
                         ['Maduk - Life.mp3', 'Sample.flac'])

    def test_search_by_seconds(self):
        mc = MusicCollection("./test_collection/", flac=True, ogg=True)
        self.assertEqual(mc.search_by_length_in_seconds('< 200'),
                         ['Sample.flac'])

    def test_search_by_year(self):
        mc = MusicCollection("./test_collection/", flac=True, ogg=True)
        self.assertEqual(
            mc.search_by_year(
                '< 2013'), ['Maduk - Life.mp3',
                            'Metrik - Freefall VIP.mp3',
                            'Lepidoptera'])

    def test_search_by_genre(self):
        mc = MusicCollection("./test_collection/", flac=True, ogg=True)
        self.assertEqual(mc.search_by_genre('Pop'),
                         ['Passenger - Let Her Go'])

    def test_search_by_album(self):
        mc = MusicCollection("./test_collection/", flac=True, ogg=True)
        self.assertEqual(mc.search_by_album('Cool'), ['2'])

    def test_search_by_artist(self):
        mc = MusicCollection("./test_collection/", flac=True, ogg=True)
        self.assertEqual(mc.search_by_artist('Maduk'),
                         ['Maduk - Life.mp3'])

    def test_search_by_name(self):
        mc = MusicCollection("./test_collection/", flac=True, ogg=True)
        self.assertEqual(
            mc.search_by_name('Let Her Go'),
            ['Passenger - Let Her Go'])


if __name__ == '__main__':
    unittest.main()
