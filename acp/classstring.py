class reverstr:
    def __init__(self,phrase):
        self.phrase = phrase

    def rev(self):
        word_list = self.phrase.split()
        print(word_list)
        word_list.reverse()
        print(word_list)
        new_rev = " ".join(word_list)
        print("the reverse string is \n",new_rev)


r1 = reverstr("arkiive is the best")
r1.rev()