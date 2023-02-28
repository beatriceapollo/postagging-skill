from mycroft import MycroftSkill, intent_handler
from adapt.intent import IntentBuilder
from nltk.tokenize import word_tokenize
import nltk



class Postagging(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('postagging.intent')
    def handle_postagging(self, message):
        self.speak_dialog('postagging')

    @intent_handler(IntentBuilder('IdentityIntent').require('identity'))
    def handle_identity_intent(self, message):
            text = message.data.get('utterance')
            tokenized_text = word_tokenize(text)
            tagged_text = nltk.pos_tag(tokenized_text)
            self.speak(print(tagged_text))

    @intent_handler(IntentBuilder('StopIntent').require('stop'))
    def handle_stop_intent(self, message):
        self.speak_dialog('stop')
         
         

def create_skill():
    return Postagging()

