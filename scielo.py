import urllib2
import codecs
import time
import wordcloud
import matplotlib.pyplot as plt
from collections import defaultdict
from bs4 import BeautifulSoup
from nltk import FreqDist
from operator import itemgetter

def extraerissues(issn):
    url = "http://www.scielo.org.mx/scielo.php?script=sci_issues&pid=" + issn + "&lng=es&nrm=iso"
    try:
        html = urllib2.urlopen(url).read()
    except:
        print "error ei"
        return ''
    soup = BeautifulSoup(html, 'html.parser')

    issues = {i.get('href') for i in soup.find_all('a') if "issuetoc" in unicode(i.get('href'))}
    return issues

def extraerarticulos(url):
    try:
        html = urllib2.urlopen(url).read()
    except:
        print "error ea"
        return ''
    soup = BeautifulSoup(html, 'html.parser')
    abstracts = {unicode(i.get('href')) for i in soup.find_all('a') if u"abstract" in unicode(i.get('href')) and u"tlng=es" in unicode(i.get('href'))}
    return abstracts

def extraerkeywords(url):
    try:
        html = urllib2.urlopen(url).read()
    except:
        print "error ek"
        return ''
    soup = BeautifulSoup(html, 'html.parser')
    texto = soup.get_text()
    return texto.partition('Palabras llave\n\t\t:\n\t\t')[2].partition('.')[0].split(';')

def keywordsrevista(issn):
    issues = extraerissues(issn)
    
    arts = []
    for i in list(issues):
        for j in list(extraerarticulos(i)):    
            arts.append(j)
        time.sleep(1)
    abstr = [] 
    for i in list(arts):
        for j in list(extraerkeywords(i)):
            abstr.append(j)
        time.sleep(1)
    abstr = [i.strip() for i in abstr]
    return abstr

def saveoutput(keywords, issn, nombre):
    filename = issn + '-' + nombre + '.txt'
    archivo = codecs.open(filename, 'w', 'utf-8')
    #nospace = [i.strip() for i in keywords]    
    archivo.write(';'.join(keywords))
    archivo.close()

def mapapalabras(issn, titulo):
    print 'Analizando ' + titulo
    kw = keywordsrevista(issn)
    print titulo + ' ya analizado'
    saveoutput(kw,issn, titulo)
    fd = FreqDist(kw)
    lista = [(k,v) for k, v in fd.iteritems()]
    ordenado = sorted(lista, key=itemgetter(1), reverse=True)
    woc = wordcloud.WordCloud(max_font_size = 40, relative_scaling=.5).generate_from_frequencies(ordenado)        
    plt.figure()
    plt.suptitle(titulo)
    #ax = plt.add_subplot(111, autoscale_on=False, xlim=(-1, 5), ylim=(-3, 5))
    #ax.annotate('pixels', xy=(0, 0), xycoords='figure fraction')
    plt.imshow(woc)
    plt.axis("off")
    plt.savefig(issn + '-' + titulo + '.png')
    