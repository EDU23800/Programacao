from lxml import etree
import urllib2

def varrerArvore(arvore, tab = "", count = 0):
    print( "%s%s" % ( tab, str( arvore.tag )  ) )
    
    for no in arvore.getchildren():
        varrerArvore(no, tab + " ", count )

downloadHtml = urllib2.urlopen("http://www.pwi.com.br")

html = etree.HTML( downloadHtml.read() )
varrerArvore(html)