MusicCollectionLibrary
======================

Да се имплементира библиотека, която работи с аудио файлове (за целите на условието: аудио=mp3) и предоставя следните възможности:

1. Инициализира се по път във файловата система, който служи за "корен" на  музикалната колекция (напр. C:\Music).
    
2. Дава статистики за музикалната колекция: общ брой аудио файлове, среден размер на аудио файл, среден брой на аудио файловете в директория.
    
3. За всеки mp3 файл предоставя информация за таговете му (тагове=ID3 тагове).
4. За всеки mp3 файл предоставя информация за релативният път в колекцията за него (напр. за C:\Music\John Coltrane\Giant Steps\Naima.mp3, релативният път е John Coltrane\Giant Steps\Naima.mp3).

5. Дава възможност да се обходи колекцията и да се открият всички файлове в нея, които не са именувани "добре".
        
6. Допълнителни статистики: средна дължина на аудио файл, най-често срещани артисти, най-често срещани стилове

7. Възможност за работа с допълнителни аудио формати: flac, ogg (и респективните формати за тагове)

8. Възможност за филтриране на песни: по година, по  дължина и др.
