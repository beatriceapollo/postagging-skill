from mycroft import MycroftSkill, intent_handler
from adapt.intent import IntentBuilder
from nltk.tokenize import word_tokenize
import nltk
from nltk.chunk import RegexpParser
from nltk import word_tokenize
from owlready2 import *
import owlready2

#carico l'ontologia all'interno dello script:
onto = get_ontology("./HBAwithEnergy.owl").load()

class Postagging(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)


    #definisco la lista di tutte le object property dell'ontologia e la stampo:
    #object_properties_list = list(onto.object_properties())
    #print(object_properties_list)

    #definisco la lista di tuple contenente le associazioni proprietà-range e la stampo:
    #associations = []
    #for o in object_properties_list:
        #associations.append((o,o.range))
        #print(associations)

    @intent_handler('postagging.intent')
    def handle_postagging(self, message):
        self.speak_dialog('postagging')

    @intent_handler(IntentBuilder('IdentityIntent').require('identity'))
    def handle_identity_intent(self, message):
            #carico l'ontologia all'interno dello script:
        onto = get_ontology("HBAwithEnergy.owl").load()

        #definisco la lista di tutte le object property dell'ontologia e la stampo:
        #object_properties_list = list(onto.object_properties())
        #print(object_properties_list)

        #definisco la lista di tuple contenente le associazioni proprietà-range e la stampo:
        #associations = []
        #for o in object_properties_list:
            #associations.append((o,o.range))
            #print(associations)
        #recupero la frase pronunciata dall'utente:
        text = message.data.get('utterance')
        #effettuo il pos tagging della frase:
        tokenized_text = word_tokenize(text)
        tagged_text = nltk.pos_tag(tokenized_text)
        #definisco il pattern P1 da riconoscere (verbo+eventuali tag qualsiasi+nome):
        #chunker = RegexpParser(r'''
        #P1:
        #{<VB.*><.*>*<NN.*>}
        #''')

        #effettuo la prima operazione di chunking e stampo l'albero risultante:
        #output = chunker.parse(tagged_text) 
        #print(output) 

        #estraggo e stampo il sottoalbero che rappresenta il pattern taggato con P1:
        #for subtree in output.subtrees(filter=lambda t: t.label() == 'P1'):
            #print(subtree) 

        #definisco il secondo pattern P2 (nome):
        #chunker2 = RegexpParser(r'''
        #P2:
        #{<NN.*>}
        #''')
                        
        #effettuo la seconda operazione di chunking sul sottoalbero di prima e stampo l'albero risultante:
        #output2 = chunker2.parse(subtree)
        #print(output2) 

        #estraggo e stampo il secondo sottoalbero che rappresenta il pattern taggato con P2:
        #for subtree2 in output2.subtrees(filter=lambda t: t.label() == 'P2'):
            #print(subtree2)

        #trasformo il sottalbero estratto in una stringa e lo stampo con la prima lettera maiuscola:
        #Concept_string = (' '.join([x[0] for x in subtree2])).capitalize()
        #print(Concept_string)

        #effettuo la ricerca del concetto estratto all'interno dell'ontologia e stampo il risultato:
        #Concept = onto.search(iri = "*"+Concept_string)
        #ConceptMatch = Concept[0]
        #print(ConceptMatch)

        #definisco la lista degli "antenati" del concetto estratto e la stampo:
        #Ancestors = list(Concept[0].ancestors())
        #print(Ancestors)

        #cerco tra gli antenati la classe che è un range di una proprietà presente nell'ontologia;
        #salvo all'interno di variabili la classe individuata come range e la proprietà associata:
        #for A in Ancestors:
            #for prop, range_list in associations:
                #if A in range_list:
                    #RangeMatch = A
                    #PropertyMatch = prop

        #stampo le variabili per verifica:
        #print(RangeMatch)
        #print(PropertyMatch)

        #definisco l'annotazione che descrive una nuova classe e la stampo:
        #class_expression = PropertyMatch.only(ConceptMatch) & PropertyMatch.some(Thing)
        #print(class_expression)

        #dichiaro la nuova classe:
        #with onto:
            #class NewClass(Thing):
                #equivalent_to = class_expression

        self.speak(print(tagged_text))

    @intent_handler(IntentBuilder('StopIntent').require('stop'))
    def handle_stop_intent(self, message):
        self.speak_dialog('stop')
         
         

def create_skill():
    return Postagging()

