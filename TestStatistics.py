import unittest

from MusicCollection import MusicCollection
from Statistics import Statistics


class TestStatistics(unittest.TestCase):
    #

    def test_(self):
        mc = MusicCollection("./test_collection/", flac=True, ogg=True)
        mcs = mc.get_statisctics()
        self.assertEqual(mcs.count, 9)
        self.assertEqual(mcs.avg_size, 4139946.777777778)
        self.assertEqual(mcs.avg_length, 259.51050070861675)
        self.assertEqual(mcs.avg_length_min, 4.325175011810279)
        self.assertEqual(mcs.max_artist, ('Andreas Ort', 2))
        self.assertEqual(mcs.max_genre, ('Electronic', 6))


if __name__ == '__main__':
    unittest.main()
