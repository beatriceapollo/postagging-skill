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
    @intent_handler(IntentBuilder('UniversityIntent').require('university'))
    def handle_university_intent(self, message):
            text = message.data.get('utterance')
            tokenized_text = word_tokenize(text)
            tagged_text = nltk.pos_tag(tokenized_text)
            self.speak(print(tagged_text))

    def stop(self):
        if self.process and self.process.poll() is None:
            self.process.terminate()
            self.process.wait()
         

def create_skill():
    return Postagging()

