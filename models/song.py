class Song:
    def __init__(self, title, bpm, key, duration):
        self.title = title
        self.bpm = bpm
        self.key = key
        self.duration = duration

    def get_energy(self):
        if self.bpm < 100:
            return "Low Energy"
        elif self.bpm <= 130:
            return "Medium Energy"
        else:
            return "High Energy"

    def get_duration_formatted(self):
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{minutes}:{seconds:02}"
    
    def matches_title(self, search):
        return search in self.title.lower()

    def is_title(self, title):
        return self.title.lower() == title.lower()