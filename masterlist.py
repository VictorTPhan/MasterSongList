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
      "https://drive.google.com/uc?id=1y1lOgV3FdGBkGMOb89rojlEE6-3haj7g&export=download",
      "https://drive.google.com/uc?id=1l1kLEzVnTqyw_TJJD6j1Oe9__FlSq_XW&export=download",
      [
        24.11, 58.44, 63.54, 91.15, 113.06, 140.96, 163.59, 190.49, 219.76,
        250.07
      ], [1, 1, 1, 1, 1, 1, 1, 1]),
    Mode(
      "https://drive.google.com/uc?id=1y1lOgV3FdGBkGMOb89rojlEE6-3haj7g&export=download",
      "https://drive.google.com/uc?id=1tpXEOTYT3KXYo1Rzc1572pv4bceqWLBQ&export=download",
      [
        24.11, 58.44, 63.54, 91.15, 113.06, 140.96, 163.59, 190.49, 219.76,
        250.07
      ], [1, 1, 1, 1, 1, 1, 1, 1]),
    Mode(
      "https://drive.google.com/uc?id=1y1lOgV3FdGBkGMOb89rojlEE6-3haj7g&export=download",
      "https://drive.google.com/uc?id=1Kx70F8BoZJUNmhgRFRgHBpqth-3l9cof&export=download",
      [
        24.11, 58.44, 63.54, 91.15, 113.06, 140.96, 163.59, 190.49, 219.76,
        250.07
      ], [1, 1, 1, 1, 1, 1, 1, 1]),
  ),
  Song(
    "Prelude Defaun", "Debussy",
    Mode(
      "https://drive.google.com/uc?id=1fzJChP7ty48i-mPSyo9YvDUbhq5j8q55&export=download",
      "https://www.free-scores.com/MP3SUPT/gurlitt-cornelius-moderato-9646-183875.mp3",
      [37.0, 53.0, 37.0, 57.0, 66.0], [1, 1, 1, 1]),
    Mode(
      "https://drive.google.com/uc?id=1fzJChP7ty48i-mPSyo9YvDUbhq5j8q55&export=download",
      "https://drive.google.com/uc?id=1usOI5H2vkh95t6FjaTd_oMHmDwfe04ss&export=download",
      [37.0, 53.0, 37.0, 57.0, 66.0], [1, 1, 1, 1]),
    Mode(
      "https://drive.google.com/uc?id=1fzJChP7ty48i-mPSyo9YvDUbhq5j8q55&export=download",
      "https://www.free-scores.com/MP3T/gurlitt-cornelius-moderato-183875.mp3",
      [37.0, 53.0, 37.0, 57.0, 66.0], [1, 1, 1, 1])),
  Song(
    "Moderato", "Cornelius Gurlitt",
    Mode(
      "https://www.free-scores.com/PDF_EN/gurlitt-cornelius-moderato-183875.pdf",
      "https://www.free-scores.com/MP3SUPT/gurlitt-cornelius-moderato-9646-183875.mp3",
      [], []),
    Mode(
      "https://www.free-scores.com/PDF_EN/gurlitt-cornelius-moderato-183875.pdf",
      "https://www.free-scores.com/MP3SUPT/gurlitt-cornelius-moderato-2967-183875.mp3",
      [], []),
    Mode(
      "https://www.free-scores.com/PDF_EN/gurlitt-cornelius-moderato-183875.pdf",
      "https://www.free-scores.com/MP3T/gurlitt-cornelius-moderato-183875.mp3",
      [], [])),
  Song(
    "Rondino", "Joseph Hadyn",
    Mode(
      "https://www.free-scores.com/PDFSUP_EN/haydn-joseph-rondino-primo-7237-181025.pdf",
      "https://www.free-scores.com/MP3SUPT/haydn-joseph-rondino-8534-181025.mp3",
      [23.69, 35.66], [1, -1]),
    Mode(
      "https://www.free-scores.com/PDFSUP_EN/haydn-joseph-rondino-secondo-6239-181025.pdf",
      "https://www.free-scores.com/MP3SUPT/haydn-joseph-rondino-4007-181025.mp3",
      [23.69, 35.66], [1, -1]),
    Mode(
      "https://www.free-scores.com/PDF_EN/haydn-joseph-rondino-181025-684.pdf",
      "https://www.free-scores.com/MP3T/haydn-joseph-rondino-181025-684.mp3",
      [23.69, 35.66], [1, -1])),
  Song(
    "Menuet", "Amadeus Mozart",
    Mode(
      "https://www.free-scores.com/PDFSUP_EN/mozart-wolfgang-amadeus-menuet-primo-3218-180183.pdf",
      "https://www.free-scores.com/MP3SUPT/mozart-wolfgang-amadeus-menuet-3256-180183.mp3",
      [46.97, 102.36, 135.04, 152.83, 165.71, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://www.free-scores.com/PDFSUP_EN/mozart-wolfgang-amadeus-menuet-secondo-3623-180183.pdf",
      "https://www.free-scores.com/MP3SUPT/mozart-wolfgang-amadeus-menuet-950-180183.mp3",
      [46.97, 102.36, 135.04, 152.83, 165.71, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://www.free-scores.com/PDF_EN/mozart-wolfgang-amadeus-menuet-180183.pdf",
      "https://www.free-scores.com/MP3T/mozart-wolfgang-amadeus-menuet-180183.mp3",
      [46.97, 102.36, 135.04, 152.83, 165.71, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5])),
  Song(
    "Concert", "Amadeus Mozart",
    Mode(
      "https://drive.google.com/uc?id=13sq4TVIH4rFYwyXEMgVgy_Otaf2yLQYr&export=download",
      "https://www.free-scores.com/MP3SUPT/mozart-wolfgang-amadeus-menuet-3256-180183.mp3",
      [46.97, 102.36, 135.04, 152.83, 165.71, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://drive.google.com/uc?id=13sq4TVIH4rFYwyXEMgVgy_Otaf2yLQYr&export=download",
      "https://www.free-scores.com/MP3SUPT/mozart-wolfgang-amadeus-menuet-3256-180183.mp3",
      [46.97, 102.36, 135.04, 152.83, 165.71, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://drive.google.com/uc?id=13sq4TVIH4rFYwyXEMgVgy_Otaf2yLQYr&export=download",
      "https://drive.google.com/uc?id=1G3csFLZZqsUdk0Fpl5xn1nXM-9vPec1l&export=download",
      [46.97, 102.36, 135.04, 152.83, 165.71, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5])),
  Song(
    "Concerto", "Billy Joel",
    Mode(
      "https://drive.google.com/uc?id=13sq4TVIH4rFYwyXEMgVgy_Otaf2yLQYr&export=download",
      "https://www.free-scores.com/MP3SUPT/mozart-wolfgang-amadeus-menuet-3256-180183.mp3",
      [46.97, 102.36, 135.04, 152.83, 165.61, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://drive.google.com/uc?id=13sq4TVIH4rFYwyXEMgVgy_Otaf2yLQYr&export=download",
      "https://www.free-scores.com/MP3SUPT/mozart-wolfgang-amadeus-menuet-3256-180183.mp3",
      [46.97, 102.36, 135.04, 152.83, 165.61, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://drive.google.com/uc?id=13sq4TVIH4rFYwyXEMgVgy_Otaf2yLQYr&export=download",
      "https://drive.google.com/uc?id=1G3csFLZZqsUdk0Fpl5xn1nXM-9vPec1l&export=download",
      [46.97, 102.36, 135.04, 152.83, 165.61, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5])),
  Song(
    "Easy piano duet", "Lopez Calvo Gabriel Alejadro",
    Mode(
      "https://drive.google.com/uc?id=1_fFAJMD5TrY1pEvdBmivJCedD01tzUBX&export=download",
      "https://drive.google.com/uc?id=1n3EBeeQQKbnn6hQSiXTkTsBqnXEh6KBj&export=download",
      [46.97, 102.36, 135.04, 152.83, 165.61, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://drive.google.com/uc?id=1_fFAJMD5TrY1pEvdBmivJCedD01tzUBX&export=download",
      "https://drive.google.com/uc?id=1n3EBeeQQKbnn6hQSiXTkTsBqnXEh6KBj&export=download",
      [46.97, 102.36, 135.04, 152.83, 165.61, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://drive.google.com/uc?id=1_fFAJMD5TrY1pEvdBmivJCedD01tzUBX&export=download",
      "https://drive.google.com/uc?id=1n3EBeeQQKbnn6hQSiXTkTsBqnXEh6KBj&export=download",
      [46.97, 102.36, 135.04, 152.83, 165.61, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5])),
  Song(
    "Whiskey in the jar", "unknown",
    Mode(
      "https://drive.google.com/uc?export=download&id=1B15P6QaO3n5AOmpqTFhiGkKFodDVFthC",
      "https://drive.google.com/uc?export=download&id=12XFjkyvKN7XlrXkayk-25aqwsknZkHmD",
      [46.97, 102.36, 135.04, 152.83, 165.61, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://drive.google.com/uc?export=download&id=1B15P6QaO3n5AOmpqTFhiGkKFodDVFthC",
      "https://drive.google.com/uc?id=1n3EBeeQQKbnn6hQSiXTkTsBqnXEh6KBj&export=download",
      [46.97, 102.36, 135.04, 152.83, 165.61, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://drive.google.com/uc?export=download&id=1B15P6QaO3n5AOmpqTFhiGkKFodDVFthC",
      "https://drive.google.com/uc?id=1n3EBeeQQKbnn6hQSiXTkTsBqnXEh6KBj&export=download",
      [46.97, 102.36, 135.04, 152.83, 165.61, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5])),
  Song(
    "Carol of the Bells", "Mykola Leontovych",
    Mode(
      "https://drive.google.com/uc?export=download&id=1LL9KanKC5vToQYn_dcXqEY6QW8p1Bf7c",
      "https://drive.google.com/uc?export=download&id=16hsrQAxORnbmPu8LwLajJ19e9JRnBvDY",
      [46.97, 102.36, 135.04, 152.83, 165.61, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://drive.google.com/uc?export=download&id=1LL9KanKC5vToQYn_dcXqEY6QW8p1Bf7c",
      "https://drive.google.com/uc?export=download&id=16hsrQAxORnbmPu8LwLajJ19e9JRnBvDY",
      [46.97, 102.36, 135.04, 152.83, 165.61, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://drive.google.com/uc?export=download&id=1LL9KanKC5vToQYn_dcXqEY6QW8p1Bf7c",
      "https://drive.google.com/uc?export=download&id=16hsrQAxORnbmPu8LwLajJ19e9JRnBvDY",
      [46.97, 102.36, 135.04, 152.83, 165.61, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5])),
      Song(
    "Piano concerto No.1", "Tchaikovsky",
    Mode(
      "https://drive.google.com/uc?export=download&id=1LL9KanKC5vToQYn_dcXqEY6QW8p1Bf7c",
      "https://drive.google.com/uc?id=1Zmbscl8jnV_gd3sCLxnE4n7ND1EB68xC/&export=download",
      [46.97, 102.36, 135.04, 152.83, 165.61, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://drive.google.com/uc?export=download&id=1LL9KanKC5vToQYn_dcXqEY6QW8p1Bf7c",
      "https://drive.google.com/uc?id=1Zmbscl8jnV_gd3sCLxnE4n7ND1EB68xC/&export=download",
      [46.97, 102.36, 135.04, 152.83, 165.61, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5]),
    Mode(
      "https://drive.google.com/uc?export=download&id=1LL9KanKC5vToQYn_dcXqEY6QW8p1Bf7c"
      "https://drive.google.com/uc?id=1Zmbscl8jnV_gd3sCLxnE4n7ND1EB68xC/&export=download",
      [46.97, 102.36, 135.04, 152.83, 165.61, 184.98, 208.62],
      [1, 1, 1, -1, 1, -3, 5])),
] # DON'T PASTE BELOW THIS LINE
