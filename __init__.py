from mycroft import MycroftSkill, intent_file_handler
from nltk.tokenize import word_tokenize
import nltk



class Postagging(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('postagging.intent')
    def handle_postagging(self, message):
        self.speak_dialog('postagging')
    def converse(self, utterances, lang):
        if utterances:
            text = utterances[0]
            tokenized_text = word_tokenize(text)
            tagged_text = nltk.pos_tag(tokenized_text)
            self.speak(tagged_text)
            return True
        if self.voc_match(utterances[0], 'stop'):
             pass
        else:
            return False 


def create_skill():
    return Postagging()

