from collections import defaultdict


class Statistics:

    """ """

    def __init__(self, audio_file_list):
        try:
            # number of audio files in root directory
            self.count = len(audio_file_list)

            # average size of audio files in root directory
            self.avg_size = sum(
                [audio.size for audio
                 in audio_file_list]) / self.count

        # average length of audio files in root directory in seconds
            self.avg_length = sum(
                [audio.length for audio
                 in audio_file_list]) / self.count

        # average length of audio files in root directory in minutes
            self.avg_length_min = self.avg_length / 60

            # most encountered artists
            max_artist = defaultdict(int)
            for audio in audio_file_list:
                max_artist[str(audio.artist)] += 1

            values = list(max_artist.values())
            keys = list(max_artist.keys())
            self.max_artist = (keys[values.index(max(values))],
                               max(values))

            # most encountered genre
            max_genre = defaultdict(int)
            for audio in audio_file_list:
                max_genre[str(audio.genre)] += 1

            values = list(max_genre.values())
            keys = list(max_genre.keys())
            self.max_genre = (keys[values.index(max(values))],
                              max(values))
        except:
            raise Exception('Oops! Something went wrong ' +
                            'at Statistics.__init__!')

    def __str__(self):
        try:
            return "Count: " + str(self.count) +\
                ", Avg Size: " + str(self.avg_size) + " bytes" +\
                ", Avg Secs: " + str(self.avg_length) + " secs" +\
                ", Avg Mins: " + str(self.avg_length_min) + " mins" +\
                ", Most Artist: " + str(self.max_artist)  +\
                ", Most Genre: " + str(self.max_genre)
        except:
            raise Exception('Oops! Cannot cast Statistics to string')
