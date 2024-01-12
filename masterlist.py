'''
NOTE FOR TIMESTAMPS AND TURNTIMES:
1. Timestamps are floats representing seconds. Do not insert integers into the timestamp list.
2. Turntime length is the length of the timestamps minus 1.
3. To go forward a page, insert a 1. There is no feature to go multiple pages forward.
4. To go back a page, insert a negative number with the amount to go back.
5. Turntimes must respect the length of the music sheet length. If the sheet is of length 3, do not have the turn times go past 3, and if you are going back a page, do not go past page 1. For example, accepted turntimes for a 3-page pdf is [1,1,1], [1,-1,1], and [1,1,-2]. [1,1,1,1], and [1,-1,-1] are not accepted.
'''

from song import Song, Mode

MASTER_LIST = [
  Song(
    "Miniature concerto",
    "Alec Rowley",
    Mode(
      "https://github.com/VictorTPhan/MasterSongList/raw/master/miniature_concerto/primo_audio.mp3",
      "https://github.com/VictorTPhan/MasterSongList/raw/master/miniature_concerto/primo_pdf.pdf",
      [
        24.11, 58.44, 63.54, 91.15, 113.06, 140.96, 163.59, 190.49, 219.76,
        250.07
      ], [1, 1, 1, 1, 1, 1, 1, 1]),
    Mode(
      "https://github.com/VictorTPhan/MasterSongList/raw/master/miniature_concerto/secondo_audio.mp3",
      "https://github.com/VictorTPhan/MasterSongList/raw/master/miniature_concerto/secondo_pdf.pdf",
      [
        24.11, 58.44, 63.54, 91.15, 113.06, 140.96, 163.59, 190.49, 219.76,
        250.07
      ], [1, 1, 1, 1, 1, 1, 1, 1]),
    Mode(
      "https://github.com/VictorTPhan/MasterSongList/raw/master/miniature_concerto/both_audio.mp3",
      "https://github.com/VictorTPhan/MasterSongList/raw/master/miniature_concerto/both_pdf.pdf",
      [
        24.11, 58.44, 63.54, 91.15, 113.06, 140.96, 163.59, 190.49, 219.76,
        250.07
      ], [1, 1, 1, 1, 1, 1, 1, 1]),
  ),
  Song(
    "Prelude Defaun", "Debussy",
    Mode(
      "https://github.com/VictorTPhan/MasterSongList/raw/master/prelude_defaun/primo_audio.mp3",
      "https://github.com/VictorTPhan/MasterSongList/raw/master/prelude_defaun/primo_pdf.pdf",
      [37.0, 53.0, 37.0, 57.0, 66.0], [1, 1, 1, 1]),
    Mode(
      "https://github.com/VictorTPhan/MasterSongList/raw/master/prelude_defaun/secondo_audio.mp3",
      "https://github.com/VictorTPhan/MasterSongList/raw/master/prelude_defaun/secondo_pdf.pdf",
      [37.0, 53.0, 37.0, 57.0, 66.0], [1, 1, 1, 1]),
    Mode(
      "https://github.com/VictorTPhan/MasterSongList/raw/master/prelude_defaun/both_audio.mp3",
      "https://github.com/VictorTPhan/MasterSongList/raw/master/prelude_defaun/both_pdf.pdf",
      [37.0, 53.0, 37.0, 57.0, 66.0], [1, 1, 1, 1])),
  Song(
    "Moderato", "Cornelius Gurlitt",
    Mode(
      "https://github.com/VictorTPhan/MasterSongList/raw/master/moderato/primo_audio.mp3",
      "https://github.com/VictorTPhan/MasterSongList/raw/master/moderato/primo_pdf.pdf",
      [], []),
    Mode(
      "https://github.com/VictorTPhan/MasterSongList/raw/master/moderato/secondo_audio.mp3",
      "https://github.com/VictorTPhan/MasterSongList/raw/master/moderato/secondo_pdf.pdf",
      [], []),
    Mode(
      "https://github.com/VictorTPhan/MasterSongList/raw/master/moderato/both_audio.mp3",
      "https://github.com/VictorTPhan/MasterSongList/raw/master/moderato/both_pdf.pdf",
      [], [])),
  Song(
    "Rondino", "Joseph Hadyn",
    Mode(
      "https://github.com/VictorTPhan/MasterSongList/raw/master/rondino/primo_audio.mp3",
      "https://github.com/VictorTPhan/MasterSongList/raw/master/rondino/primo_pdf.pdf",
      [23.69, 35.66], [1, -1]),
    Mode(
      "https://github.com/VictorTPhan/MasterSongList/raw/master/rondino/secondo_audio.mp3",
      "https://github.com/VictorTPhan/MasterSongList/raw/master/rondino/secondo_pdf.pdf",
      [23.69, 35.66], [1, -1]),
    Mode(
      "https://github.com/VictorTPhan/MasterSongList/raw/master/rondino/both_audio.mp3",
      "https://github.com/VictorTPhan/MasterSongList/raw/master/rondino/both_pdf.pdf",
      [23.69, 35.66], [1, -1])),
  Song(
    "Menuet", "Amadeus Mozart",
    Mode(
      "https://github.com/VictorTPhan/MasterSongList/raw/master/menuet/primo_audio.mp3",
      "https://github.com/VictorTPhan/MasterSongList/raw/master/menuet/primo_pdf.pdf",
      [46.97, 102.36, 135.04, 152.83, 165.71, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://github.com/VictorTPhan/MasterSongList/raw/master/menuet/secondo_audio.mp3",
      "https://github.com/VictorTPhan/MasterSongList/raw/master/menuet/secondo_pdf.pdf",
      [46.97, 102.36, 135.04, 152.83, 165.71, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://github.com/VictorTPhan/MasterSongList/raw/master/menuet/both_audio.mp3",
      "https://github.com/VictorTPhan/MasterSongList/raw/master/menuet/both_pdf.pdf",
      [46.97, 102.36, 135.04, 152.83, 165.71, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5])),
  Song(
    "Concert", "Amadeus Mozart",
    Mode(
      "https://github.com/VictorTPhan/MasterSongList/raw/master/concert/primo_audio.mp3",
      "https://github.com/VictorTPhan/MasterSongList/raw/master/concert/primo_pdf.pdf",
      [46.97, 102.36, 135.04, 152.83, 165.71, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://github.com/VictorTPhan/MasterSongList/raw/master/concert/secondo_audio.mp3",
      "https://github.com/VictorTPhan/MasterSongList/raw/master/concert/secondo_pdf.pdf",
      [46.97, 102.36, 135.04, 152.83, 165.71, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://github.com/VictorTPhan/MasterSongList/raw/master/concert/both_audio.mp3",
      "https://github.com/VictorTPhan/MasterSongList/raw/master/concert/both_pdf.pdf",
      [46.97, 102.36, 135.04, 152.83, 165.71, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5])),
  Song(
    "Concerto", "Billy Joel",
    Mode(
      "https://github.com/VictorTPhan/MasterSongList/raw/master/concerto/primo_audio.mp3",
      "https://github.com/VictorTPhan/MasterSongList/raw/master/concerto/primo_pdf.pdf",
      [46.97, 102.36, 135.04, 152.83, 165.61, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://github.com/VictorTPhan/MasterSongList/raw/master/concerto/secondo_audio.mp3",
      "https://github.com/VictorTPhan/MasterSongList/raw/master/concerto/secondo_pdf.pdf",
      [46.97, 102.36, 135.04, 152.83, 165.61, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://github.com/VictorTPhan/MasterSongList/raw/master/concerto/both_audio.mp3",
      "https://github.com/VictorTPhan/MasterSongList/raw/master/concerto/both_pdf.pdf",
      [46.97, 102.36, 135.04, 152.83, 165.61, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5])),
  Song(
    "Easy piano duet", "Lopez Calvo Gabriel Alejadro",
    Mode(
      "https://github.com/VictorTPhan/MasterSongList/raw/master/easy_piano_duet/primo_audio.mp3",
      "https://github.com/VictorTPhan/MasterSongList/raw/master/easy_piano_duet/primo_pdf.pdf",
      [46.97, 102.36, 135.04, 152.83, 165.61, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://github.com/VictorTPhan/MasterSongList/raw/master/easy_piano_duet/secondo_audio.mp3",
      "https://github.com/VictorTPhan/MasterSongList/raw/master/easy_piano_duet/secondo_pdf.pdf",
      [46.97, 102.36, 135.04, 152.83, 165.61, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://github.com/VictorTPhan/MasterSongList/raw/master/easy_piano_duet/both_audio.mp3",
      "https://github.com/VictorTPhan/MasterSongList/raw/master/easy_piano_duet/both_pdf.pdf",
      [46.97, 102.36, 135.04, 152.83, 165.61, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]))
]
