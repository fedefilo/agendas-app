# -*- coding: utf-8 -*-
import urllib2
import time
from bs4 import BeautifulSoup


def extraer_articulos(conicet_id):
    url_art = "http://www.conicet.gov.ar/new_scp/detalle.php?keywords=&id=" + str(conicet_id) + "&articulos=yes"
    response = urllib2.urlopen(url_art)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    lista = []
    for link in soup.find_all('a'):
        url = link.get('href')
        if url.startswith('detalle.php') and 'art_id' in url:
            url = 'http://www.conicet.gov.ar/new_scp/' + url
            lista.append(url)
    return lista   
    
def info_articulos(url):
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    labels = soup.find_all('div', attrs={"class": "contenido_label"})
    info = soup.find_all('div', attrs={"class": "contenido_label_info"})
    print labels, info
    if len(labels) != len(info):
        raise IndexError('tamaños no coinciden')
    info_art = {}
    for i in range(len(labels)):
        info_art.update({labels[i].text: info[i].text})
    # extraer año
    info_art.update({'anio': info_art['Referencias:'].partition('o: ')[2].partition(' ')[0]})
    return info_art


def datos_persona(id_conicet):
    urls = extraer_articulos(id_conicet)
    datos_arts = []
    for url in urls:
        dict_art = info_articulos(url)
        datos_arts.append(dict_art)
        time.sleep(0.2)
    return datos_arts
    
