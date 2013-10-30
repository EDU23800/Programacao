from lxml import etree
import urllib2

def varrerArvore(arvore, tab = "", count = 0):
    if( str( arvore.tag ).upper() == "IMG" ):
        teste = str( arvore.attrib ).split( "'src':" )
        if( teste!=None ):
            print( teste[1] )
    
    for no in arvore.getchildren():
        varrerArvore(no, tab + " ", count )

downloadHtml = urllib2.urlopen("http://www.pwi.com.br")

html = etree.HTML( downloadHtml.read() )
varrerArvore(html)

#teste = open("html.html").read()
#if( element.tag == "img" ):
#   print( "%s", str( element.attrib ) )
# element.tag, element.text, element.tail, element.attrib