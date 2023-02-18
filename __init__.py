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
    @intent_handler(IntentBuilder('UniversityIntent').require('university').require('stop'))
    def handle_university_intent(self, message):
        if self.voc_match(message.data['utterances'], 'stop'):
            pass
        else:
            text = message.data.get('utterance')
            tokenized_text = word_tokenize(text)
            tagged_text = nltk.pos_tag(tokenized_text)
            self.speak(print(tagged_text))


def create_skill():
    return Postagging()

