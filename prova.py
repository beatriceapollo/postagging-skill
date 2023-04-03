from owlready2 import *

onto = get_ontology("file://./HBAwithEnergy.owl").load()
print(list(onto.object_properties()))