from mycroft import MycroftSkill, intent_file_handler


class Postagging(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('postagging.intent')
    def handle_postagging(self, message):
        self.speak_dialog('postagging')


def create_skill():
    return Postagging()

