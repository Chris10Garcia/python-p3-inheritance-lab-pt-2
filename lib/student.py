class Student:
    def __init__(self):
        self.greeting = "Hey there! I'm so excited to learn stuff."
        self.attenion = "Pick me!"

    def hello(self):
        print(self.greeting)

    def raise_hand(self):
        print(self.attenion)

class ChattyStudent(Student):
    def __init__(self):
        super().__init__()

    def hello(self):
        super().hello()
        self.greeting = "How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died..."
        super().hello()

    def raise_hand(self):
        for i in range (0, 10): super().raise_hand()

