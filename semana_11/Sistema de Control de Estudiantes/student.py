class Student:
    def __init__(self, name, score_1):
        self.name = name
        self.score_1 = score_1

    def to_dict(self):
        return {
            "name": self.name,
            "score_1": self.score_1
        }
