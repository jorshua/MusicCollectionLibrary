from os.path import relpath, getsize, splitext
from mutagen import File
from mutagen.easyid3 import EasyID3


class AudioFile:

    """ """

    def __init__(self, audio_path, audio_name, root_directory):
        try:
            self.audio_path = audio_path
            self.relpath = relpath(audio_path, root_directory)
            self.size = getsize(audio_path)

            self.audio_file = File(self.audio_path)

            self.length = self.audio_file.info.length
            self.length_min = self.audio_file.info.length / 60

            self.audio_info = self.audio_file.tags

            if splitext(self.relpath)[1] == '.mp3':
                self.audio_info = EasyID3(self.audio_path)

            if 'title' in self.audio_info:
                self.name = self.audio_info['title'][0]
            else:
                self.name = audio_name

            if 'artist' in self.audio_info:
                self.artist = self.audio_info['artist'][0]
            else:
                self.artist = "N/A"

            if 'album' in self.audio_info:
                self.album = self.audio_info['album'][0]
            else:
                self.album = "N/A"

            if 'genre' in self.audio_info:
                self.genre = self.audio_info['genre'][0]
            else:
                self.genre = "N/A"

            if 'date' in self.audio_info:
                self.year = self.audio_info['date'][0]
            else:
                self.year = "N/A"

        except:
            raise Exception('Oops! Something went wrong ' +
                            'at MusicCollection.__init__!')

    def __str__(self):
        try:
            return "Path: " + self.audio_path +\
                ", Realtive Path: " + self.relpath +\
                ", Size: " + str(self.size) + " bytes" +\
                ", Length: " + str(self.length) + " seconds" +\
                ",  " + str(self.length_min) + " minutes" +\
                ", Name: " + self.name +\
                ", Artist: " + self.artist +\
                ", Album: " + self.album +\
                ", Genre: " + str(self.genre) +\
                ", Year: " + str(self.year)
        except:
            raise Exception('Oops! Cannot cast AudioFile to string')

    def get_relative_path(self):
        try:
            return self.relpath
        except:
            raise Exception('Oops! Something went wrong ' +
                            'at get_relative_path!')

    def get_ID3_tags(self):
        try:
            return self.audio_info
        except:
            raise Exception('Oops! Something went wrong ' +
                            'at get_ID3_tags!')

    def check_name(self):
        try:
            if "/" + self.artist + "/" not in self.relpath:
                if self.artist != "N/A":
                    return False

            if "/" + self.name + "/" not in self.relpath:
                if self.name != "N/A":
                    return False

            return True
        except:
            raise Exception('Oops! Something went wrong ' +
                            'at check_name!')
