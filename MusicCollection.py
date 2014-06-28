from AudioFile import AudioFile
from Statistics import Statistics
from os import listdir
from os.path import exists, normcase, join, splitext, isdir
from re import match, compile


class MusicCollection:

    """ """

    def __init__(self, root_directory,
                 mp3=True, flac=False, ogg=False):
        try:
            if(exists(root_directory)):
                self.root_directory = root_directory

                # set audio formats for processing
                self.process_mp3 = mp3
                self.process_flac = flac
                self.process_ogg = ogg

                # read root directory for audio files
                self.audio_files = MusicCollection.get_audio_file_list(
                    root_directory, self.prepare_extension_filter())
            else:
                # throw dir not exist exception
                raise Exception('Directory "' + root_directory +
                                '" does not exist!')
        except:
            raise Exception('Oops! Something went wrong ' +
                            'at MusicCollection.__init__!')

    def get_statisctics(self):
        """Return audio info for audio files in root directory"""
        try:
            return Statistics(self.audio_files)
        except:
            raise Exception('Oops! Something went wrong ' +
                            'at get_statisctics!')

    def get_incorrect_named_audio_files(self):
        try:
            return [x.relpath for x in self.audio_files
                    if not x.check_name()]
        except:
            raise Exception(
                'Oops! Something went wrong ' +
                'at get_incorrect_named_audio_files!')

    def get_ID3_tags(self):
        try:
            return [x.get_ID3_tags() for x in self.audio_files]
        except:
            raise Exception('Oops! Something went wrong ' +
                            'at get_ID3_tags!')

    def refresh_audio_file_list(self):
        """Reload root directory content"""
        try:
            self.audio_files = MusicCollection.get_audio_file_list(
                root_directory, prepare_extension_filter())
        except:
            raise Exception('Oops! Something went wrong ' +
                            'at refresh_audio_file_list!')

    def prepare_extension_filter(self):
        """Prepare extension list based on extension flags"""
        try:
            file_ext_list = []
            if self.process_mp3:
                file_ext_list.append(".mp3")
            if self.process_flac:
                file_ext_list.append(".flac")
            if self.process_ogg:
                file_ext_list.append(".ogg")
            return file_ext_list
        except:
            raise Exception('Oops! Something went wrong ' +
                            'at prepare_extension_filter!')

    @classmethod
    def get_audio_file_list(cls, root_directory, file_ext_list):
        try:
            return [AudioFile(name[0], name[1], root_directory)
                    for name in
                    MusicCollection.list_directory(root_directory,
                                                   file_ext_list)]
        except:
            raise Exception('Oops! Something went wrong ' +
                            'at get_audio_file_list!')

    @classmethod
    def list_directory(cls, directory, file_ext_list):
        "Get list of file paths for files of particular extensions"
        try:
            fileList = [normcase(f)
                        for f in listdir(directory)]

            dirList = [join(directory, f) for f in fileList
                       if isdir(join(directory, f))]

            fileList = [(join(directory, f), f)
                        for f in fileList
                        if splitext(f)[1] in file_ext_list]

            [fileList.extend(
                MusicCollection.list_directory(d, file_ext_list))
             for d in dirList]

            return fileList
        except:
            raise Exception('Oops! Something went wrong ' +
                            'at list_directory!')

    def search_by_length_in_minutes(self, length_filter):
        "Filter is string containing <,<=,>,>= and value in minutes"
        try:
            return eval('[x.name for x in self.audio_files ' +
                        'if x.length_min ' + length_filter + ']')
        except:
            raise Exception('Oops! Something went wrong ' +
                            'at search_by_length_in_minutes!')

    def search_by_length_in_seconds(self, length_filter):
        "Filter is string containing <,<=,>,>= and value in seconds"
        try:
            return eval('[x.name for x in self.audio_files ' +
                        'if x.length ' + length_filter + ']')
        except:
            raise Exception('Oops! Something went wrong ' +
                            'at search_by_length_in_seconds!')

    def search_by_year(self, year_filter):
        "Filter is string containing <,<=,>,>= and value"
        try:
            return eval('[x.name for x in self.audio_files ' +
                        'if x.year != "N/A" and int(x.year) ' +
                        year_filter + ']')
        except:
            raise Exception('Oops! Something went wrong ' +
                            'at search_by_year!')

    def search_by_genre(self, genre):
        try:
            return [x.name for x in self.audio_files
                    if str(match(compile('.*' + genre + '.*'),
                                 x.genre)) != 'None']
        except:
            raise Exception('Oops! Something went wrong ' +
                            'at search_by_genre!')

    def search_by_album(self, album):
        try:
            return [x.name for x in self.audio_files
                    if str(match(compile('.*' + album + '.*'),
                                 x.album)) != 'None']
        except:
            raise Exception('Oops! Something went wrong ' +
                            'at search_by_album!')

    def search_by_artist(self, artist):
        try:
            return [x.name for x in self.audio_files
                    if str(match(compile('.*' + artist + '.*'),
                                 x.artist)) != 'None']
        except:
            raise Exception('Oops! Something went wrong ' +
                            'at search_by_artist!')

    def search_by_name(self, name):
        try:
            return [x.name for x in self.audio_files
                    if str(match(compile('.*' + name + '.*'),
                                 x.name)) != 'None']
        except:
            raise Exception('Oops! Something went wrong ' +
                            'at search_by_name!')
