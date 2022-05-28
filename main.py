class Student:
    # [assignment] Skeleton class. Add your code here

    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)


J = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)
print("My Name is", J.name)
print("I am", J.age, "years old")
print("My track is", J.tracks[1])


def change_items(self, name, age, track, score):
    self.name = str(name)
    self.age = int(age)
    self.tracks = list(track)
    self.score = float(score)


add = Student(name="Peter", age=34, tracks=["product design"], score=30.20)
print("My new name is", add.name)
print("My new age is ", add.age)
print("My new track is ", add.tracks)
print("My new score is ", add.score)



