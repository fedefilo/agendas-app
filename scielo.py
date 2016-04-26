import urllib2
import time
from collections import defaultdict
from bs4 import BeautifulSoup


def extraerissues(issn):
    url = "http://www.scielo.org.mx/scielo.php?script=sci_issues&pid=" + issn + "&lng=es&nrm=iso"
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    issues = {i.get('href') for i in soup.find_all('a') if "issuetoc" in str(i.get('href'))}
    return issues

def extraerarticulos(url):
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    abstracts = {i.get('href') for i in soup.find_all('a') if "abstract" in str(i.get('href')) and "tlng=es" in str(i.get('href'))}
    return abstracts

def extraerkeywords(url):
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    texto = soup.get_text()
    return texto.partition('Palabras llave\n\t\t:\n\t\t')[2].partition('.')[0].split(';')

def keywordsrevista(issn):
    issues = extraerissues(issn)
    
    arts = []
    for i in list(issues):    
        arts.append(list(extraerarticulos(i)))
        time.sleep(1)
    abstr = [] 
    for i in list(abstr):
        abstr.append(list(extraerarticulos(i)))
        time.sleep(1)
    kw = []    
    for i in list(abstracts):
        kw.append(extraerkeywords(i))
        time.sleep(1)

    keywords = []        
    for i in kw:
        for j in i:
            keywords.append(j)
    return keywords 