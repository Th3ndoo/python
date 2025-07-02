# flashcard application

class flashcard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return f"{self.word}({self.meaning})"
    
print("welcoe to flash card application")
flash = []
while True:
    word = input("enter the word")
    meaning = input("enter the meaning") 
    flash.append(flashcard(word,meaning))      
    ch = input("do you want to continue (y/n)")
    if ch.lower() == 'n':
        break

for i in flash:
    print("> ",i)         