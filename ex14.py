class Prompt(object):

    def __init__(self, user_name, script, likes, lives, computer):
        self.user_name = user_name
        self.script = script
        self.likes = likes
        self.lives = lives
        self.computer = computer

    def output_script(self):
        return "Hi {}, I'm the {} script. \
I'd like to ask you a few questions. \
Do you like me {}?".format(self.user_name, self.script, self.user_name)

    def output_main(self):
        return "Alright, so you said {} about liking me. \
You live in {}.  Not sure where that is. \
And you have a {} computer.  Nice.".format(self.likes, self.lives, self.computer)

# user_name = raw_input("username: ")
# script = raw_input("script name: ")
# likes = raw_input("do you like the script: ")
# lives = raw_input("where do you live: ")
# computer = raw_input("what kind of computer do you have: ")

# test = Prompt(user_name, script, likes, lives, computer)
# print test.output_script()
# print test.output_main()
