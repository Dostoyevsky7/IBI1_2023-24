#import datetime to record time
import datetime

#use SAX
SAX_start = datetime.datetime.now()
import xml.sax
class TermHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.namespace = ''
        self.currentElement = ''
        self.mf = 0
        self.bp = 0
        self.cc = 0
    def processingInstruction(self, target, data):
        pass
    def setDocumentLocator(self, locator):
        pass
    def startElement(self, tag, attribute):
        if tag == 'namespace':
            self.currentElement = tag
    def characters(self, content):
        if self.currentElement == 'namespace':
            self.namespace = content
    def endElement(self, tag):
        if self.currentElement == 'namespace':
            if self.namespace == 'molecular_function':
                self.mf += 1
            elif self.namespace == 'biological_process':
                self.bp += 1
            elif self.namespace == 'cellular_component':
                self.cc += 1
parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces,0)
handler = TermHandler()
parser.setContentHandler(handler)
parser.parse('go_obo.xml')
print('molecular function: ', handler.mf)
print('biological process: ', handler.bp)
print('cellular component: ', handler.cc)
SAX_end = datetime.datetime.now()

#use DOM
DOM_start = datetime.datetime.now()
import xml.dom.minidom
import xml.sax.handler
DOMTree = xml.dom.minidom.parse('go_obo.xml')
collection = DOMTree.documentElement
GO = collection.getElementsByTagName('term')
mf = 0
bp = 0
cc = 0
for go in GO:
    ontology = go.getElementsByTagName('namespace')[0].firstChild.nodeValue
    if ontology == 'molecular_function':
        mf += 1
    elif ontology == 'biological_process':
        bp += 1
    elif ontology == 'cellular_component':
        cc += 1
print('molecular function: ', mf)
print('biological process: ', bp)
print('cellular component: ', cc)
DOM_end = datetime.datetime.now()

#compare the time of SAX & DOM
SAX_time = SAX_end - SAX_start
DOM_time = DOM_end - DOM_start
print(SAX_time, DOM_time)
if SAX_time < DOM_time:
    print('SAX is faster')
else:
    print('DOM is faster') 
#SAX=0:00:01.436375, DOM=0:00:06.795283, SAX is fater than DOM

#draw pictures of three types of onthologies in a pie chart
import numpy as np
import matplotlib.pyplot as plt
import xml.dom.minidom
import xml.sax.handler
DOMTree = xml.dom.minidom.parse('go_obo.xml')
collection = DOMTree.documentElement
GO = collection.getElementsByTagName('term')
mf = 0
bp = 0
cc = 0
for go in GO:
    ontology = go.getElementsByTagName('namespace')[0].firstChild.nodeValue
    if ontology == 'molecular_function':
        mf += 1
    elif ontology == 'biological_process':
        bp += 1
    elif ontology == 'cellular_component':
        cc += 1
print('molecular function: ', mf)
print('biological process: ', bp)
print('cellular component: ', cc)
onto_lable = ['molecular_function', 'biological_process', 'cellular_component']
explode1 = [0,0,0]
number = [mf, bp,cc]
plt.figure()
plt.pie(number, labels = onto_lable, explode = explode1)
plt.title('a pie chart of proportions of each ontology')
plt.show()
plt.clf()

#draw a picture of bar chart
score = [mf, bp, cc] # return a list, randints from 1 to 7, 3 randints in total
ind = ['molecular_function', 'biological_process', 'cellular_component']
width = 0.5
plt.figure()
plt.bar(ind, score, width) # yerr is standard error
plt.ylabel("scores")
plt.title("Scores of groups")
plt.xticks(ind)
plt.show()
plt.clf()