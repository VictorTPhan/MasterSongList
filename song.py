class Mode:

  def __init__(self, pdf, audio, turnTimeStamps, pageTurns):
    self.pdf = pdf
    self.audio = audio
    self.turnTimeStamps = turnTimeStamps
    self.pageTurns = pageTurns  #list of integers
    #to go forward a page, enter 1
    #to turn back a page, element should be a negative number with amount to turn back (-1, -4, -3)


class Song:

  def __init__(self, name, composer, primo, secondo, both):
    self.dict = {}
    self.dict["name"] = name
    self.dict["composer"] = composer
    self.dict["primo"] = {
      "pdf": primo.pdf,
      "audio": primo.audio,
      "turnTimeStamps": primo.turnTimeStamps,
      "turnPages": primo.pageTurns
    }
    self.dict["secondo"] = {
      "pdf": secondo.pdf,
      "audio": secondo.audio,
      "turnTimeStamps": secondo.turnTimeStamps,
      "turnPages": secondo.pageTurns
    }
    self.dict["both"] = {
      "pdf": both.pdf,
      "audio": both.audio,
      "turnTimeStamps": both.turnTimeStamps,
      "turnPages": both.pageTurns
    }
