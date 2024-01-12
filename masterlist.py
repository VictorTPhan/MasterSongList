'''
NOTE FOR TIMESTAMPS AND TURNTIMES:
1. Timestamps are floats representing seconds. Do not insert integers into the timestamp list.
2. Turntime length is the length of the timestamps minus 1.
3. To go forward a page, insert a 1. There is no feature to go multiple pages forward.
4. To go back a page, insert a negative number with the amount to go back.
5. Turntimes must respect the length of the music sheet length. If the sheet is of length 3, do not have the turn times go past 3, and if you are going back a page, do not go past page 1. For example, accepted turntimes for a 3-page pdf.pdf is [1,1,1], [1,-1,1], and [1,1,-2]. [1,1,1,1], and [1,-1,-1] are not accepted.
'''

from song import Song, Mode

MASTER_LIST = [
  Song(
    "Miniature concerto",
    "Alec Rowley",
    Mode(
      "https://emma-server.onrender.com/miniature_concerto/primo_pdf.pdf",
      "https://emma-server.onrender.com/miniature_concerto/primo_audio.mp3",
      [
        24.11, 58.44, 63.54, 91.15, 113.06, 140.96, 163.59, 190.49, 219.76,
        250.07
      ], [1, 1, 1, 1, 1, 1, 1, 1]),
    Mode(
      "https://emma-server.onrender.com/miniature_concerto/secondo_pdf.pdf",
      "https://emma-server.onrender.com/miniature_concerto/secondo_audio.mp3",
      [
        24.11, 58.44, 63.54, 91.15, 113.06, 140.96, 163.59, 190.49, 219.76,
        250.07
      ], [1, 1, 1, 1, 1, 1, 1, 1]),
    Mode(
      "https://emma-server.onrender.com/miniature_concerto/both_pdf.pdf",
      "https://emma-server.onrender.com/miniature_concerto/both_audio.mp3",
      [
        24.11, 58.44, 63.54, 91.15, 113.06, 140.96, 163.59, 190.49, 219.76,
        250.07
      ], [1, 1, 1, 1, 1, 1, 1, 1]),
  ),
  Song(
    "Prelude Defaun", "Debussy",
    Mode(
      "https://emma-server.onrender.com/prelude_defaun/primo_pdf.pdf",
      "https://emma-server.onrender.com/prelude_defaun/primo_audio.mp3",
      [37.0, 53.0, 37.0, 57.0, 66.0], [1, 1, 1, 1]),
    Mode(
      "https://emma-server.onrender.com/prelude_defaun/secondo_pdf.pdf",
      "https://emma-server.onrender.com/prelude_defaun/secondo_audio.mp3",
      [37.0, 53.0, 37.0, 57.0, 66.0], [1, 1, 1, 1]),
    Mode(
      "https://emma-server.onrender.com/prelude_defaun/both_pdf.pdf",
      "https://emma-server.onrender.com/prelude_defaun/both_audio.mp3",
      [37.0, 53.0, 37.0, 57.0, 66.0], [1, 1, 1, 1])),
  Song(
    "Moderato", "Cornelius Gurlitt",
    Mode(
      "https://emma-server.onrender.com/moderato/primo_pdf.pdf",
      "https://emma-server.onrender.com/moderato/primo_audio.mp3",
      [], []),
    Mode(
      "https://emma-server.onrender.com/moderato/secondo_pdf.pdf",
      "https://emma-server.onrender.com/moderato/secondo_audio.mp3",
      [], []),
    Mode(
      "https://emma-server.onrender.com/moderato/both_pdf.pdf",
      "https://emma-server.onrender.com/moderato/both_audio.mp3",
      [], [])),
  Song(
    "Rondino", "Joseph Hadyn",
    Mode(
      "https://emma-server.onrender.com/rondino/primo_pdf.pdf",
      "https://emma-server.onrender.com/rondino/primo_audio.mp3",
      [23.69, 35.66], [1, -1]),
    Mode(
      "https://emma-server.onrender.com/rondino/secondo_pdf.pdf",
      "https://emma-server.onrender.com/rondino/secondo_audio.mp3",
      [23.69, 35.66], [1, -1]),
    Mode(
      "https://emma-server.onrender.com/rondino/both_pdf.pdf",
      "https://emma-server.onrender.com/rondino/both_audio.mp3",
      [23.69, 35.66], [1, -1])),
  Song(
    "Menuet", "Amadeus Mozart",
    Mode(
      "https://emma-server.onrender.com/menuet/primo_pdf.pdf",
      "https://emma-server.onrender.com/menuet/primo_audio.mp3",
      [46.97, 102.36, 135.04, 152.83, 165.71, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://emma-server.onrender.com/menuet/secondo_pdf.pdf",
      "https://emma-server.onrender.com/menuet/secondo_audio.mp3",
      [46.97, 102.36, 135.04, 152.83, 165.71, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://emma-server.onrender.com/menuet/both_pdf.pdf",
      "https://emma-server.onrender.com/menuet/both_audio.mp3",
      [46.97, 102.36, 135.04, 152.83, 165.71, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5])),
  Song(
    "Concert", "Amadeus Mozart",
    Mode(
      "https://emma-server.onrender.com/concert/primo_pdf.pdf",
      "https://emma-server.onrender.com/concert/primo_audio.mp3",
      [46.97, 102.36, 135.04, 152.83, 165.71, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://emma-server.onrender.com/concert/secondo_pdf.pdf",
      "https://emma-server.onrender.com/concert/secondo_audio.mp3",
      [46.97, 102.36, 135.04, 152.83, 165.71, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://emma-server.onrender.com/concert/both_pdf.pdf",
      "https://emma-server.onrender.com/concert/both_audio.mp3",
      [46.97, 102.36, 135.04, 152.83, 165.71, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5])),
  Song(
    "Concerto", "Billy Joel",
    Mode(
      "https://emma-server.onrender.com/concerto/primo_pdf.pdf",
      "https://emma-server.onrender.com/concerto/primo_audio.mp3",
      [46.97, 102.36, 135.04, 152.83, 165.61, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://emma-server.onrender.com/concerto/secondo_pdf.pdf",
      "https://emma-server.onrender.com/concerto/secondo_audio.mp3",
      [46.97, 102.36, 135.04, 152.83, 165.61, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://emma-server.onrender.com/concerto/both_pdf.pdf",
      "https://emma-server.onrender.com/concerto/both_audio.mp3",
      [46.97, 102.36, 135.04, 152.83, 165.61, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5])),
  Song(
    "Easy piano duet", "Lopez Calvo Gabriel Alejadro",
    Mode(
      "https://emma-server.onrender.com/easy_piano_duet/primo_pdf.pdf",
      "https://emma-server.onrender.com/easy_piano_duet/primo_audio.mp3",
      [46.97, 102.36, 135.04, 152.83, 165.61, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://emma-server.onrender.com/easy_piano_duet/secondo_pdf.pdf",
      "https://emma-server.onrender.com/easy_piano_duet/secondo_audio.mp3",
      [46.97, 102.36, 135.04, 152.83, 165.61, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://emma-server.onrender.com/easy_piano_duet/both_pdf.pdf",
      "https://emma-server.onrender.com/easy_piano_duet/both_audio.mp3",
      [46.97, 102.36, 135.04, 152.83, 165.61, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]))
]
