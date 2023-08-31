class MailMerge:
    def __init__(self, base_letter_addr, names_addr, letter_addr, place_holder):
        self.base_letter_addr = base_letter_addr
        self.names_addr = names_addr
        self.letter_addr = letter_addr
        self.place_holder = place_holder
        self.base_letter = self.template_letter()
        self.name_list = self.create_name_list()

    def template_letter(self):
        with open(self.base_letter_addr, mode="r") as f:
            content = f.read()
            return content

    def create_name_list(self):
        with open(self.names_addr, mode="r") as f:
            names = f.read().split("\n")
            return names

    def create_letters(self):
        for name in self.name_list:
            letter = self.base_letter.replace(self.place_holder, name)
            with open(f"{self.letter_addr}/letter_for_{name}.txt", mode="w") as f:
                f.write(letter)



