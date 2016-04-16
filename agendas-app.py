# -*- coding: utf-8 -*-
import urllib2
import time
from collections import defaultdict
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
    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    labels = soup.find_all('div', attrs={"class": "contenido_label"})
    info = soup.find_all('div', attrs={"class": "contenido_label_info"})
    if len(labels) != len(info):
        raise IndexError('tamaños no coinciden')
    info_art = {}
    for i in range(len(labels)):
        info_art.update({labels[i].text: info[i].text})
    # extraer año
    info_art.update({'anio': info_art['Referencias:'].partition('o: ')[2].partition(' ')[0]})
    return info_art

def extraer_libros(conicet_id):
    url_art = "http://www.conicet.gov.ar/new_scp/detalle.php?keywords=&id=" + str(conicet_id) + "&libros=yes"
    response = urllib2.urlopen(url_art)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    lista = []
    for link in soup.find_all('a'):
        url = link.get('href')
        if url.startswith('detalle.php') and 'lib_id' in url:
            url = 'http://www.conicet.gov.ar/new_scp/' + url
            lista.append(url)
    return lista   

def info_libros(url):
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    labels = soup.find_all('div', attrs={"class": "contenido_label"})
    info = soup.find_all('div', attrs={"class": "contenido_label_info"})
    if len(labels) != len(info):
        raise IndexError('tamaños no coinciden')
    info_lib = {}
    for i in range(len(labels)):
        info_lib.update({labels[i].text: info[i].text})
    # extraer año
    info_lib.update({'anio': info_lib['Referencias:'].partition('o: ')[2].partition(' ')[0]})
    return info_lib

def extraer_capitulos(conicet_id):
    url_art = "http://www.conicet.gov.ar/new_scp/detalle.php?keywords=&id=" + str(conicet_id) + "&capitulos=yes"
    response = urllib2.urlopen(url_art)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    lista = []
    for link in soup.find_all('a'):
        url = link.get('href')
        if url.startswith('detalle.php') and 'capit_id' in url:
            url = 'http://www.conicet.gov.ar/new_scp/' + url
            lista.append(url)
    return lista   

def info_capitulos(url):
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    labels = soup.find_all('div', attrs={"class": "contenido_label"})
    info = soup.find_all('div', attrs={"class": "contenido_label_info"})
    if len(labels) != len(info):
        raise IndexError('tamaños no coinciden')
    info_cap = {}
    for i in range(len(labels)):
        info_cap.update({labels[i].text: info[i].text})
    # extraer año
    info_cap.update({'anio': info_cap['Referencias:'].partition('o: ')[2].partition(' ')[0]})
    return info_cap

def extraer_congresos(conicet_id):
    url_art = "http://www.conicet.gov.ar/new_scp/detalle.php?keywords=&id=" + str(conicet_id) + "&congresos=yes"
    response = urllib2.urlopen(url_art)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    lista = []
    for link in soup.find_all('a'):
        url = link.get('href')
        if url.startswith('detalle.php') and 'congr_id' in url:
            url = 'http://www.conicet.gov.ar/new_scp/' + url
            lista.append(url)
    return lista   

def info_congresos(url):
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    labels = soup.find_all('div', attrs={"class": "contenido_label"})
    info = soup.find_all('div', attrs={"class": "contenido_label_info"})
    if len(labels) != len(info):
        raise IndexError('tamaños no coinciden')
    info_congr = {}
    for i in range(len(labels)):
        info_congr.update({labels[i].text: info[i].text})        
    # extraer año
    info_congr.update({'anio': info_congr[u'Reuni\xf3n:'][-4:]})
    return info_congr

def extraer_convenios(conicet_id):
    url_art = "http://www.conicet.gov.ar/new_scp/detalle.php?keywords=&id=" + str(conicet_id) + "&convenios=yes"
    response = urllib2.urlopen(url_art)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    lista = []
    for link in soup.find_all('a'):
        url = link.get('href')
        if url.startswith('detalle.php') and 'conv_id' in url:
            url = 'http://www.conicet.gov.ar/new_scp/' + url
            lista.append(url)
    return lista   

def info_convenios(url):
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    labels = soup.find_all('div', attrs={"class": "contenido_label"})
    info = soup.find_all('div', attrs={"class": "contenido_label_info"})
    if len(labels) != len(info):
        raise IndexError('tamaños no coinciden')
    info_conv = {}
    for i in range(len(labels)):
        info_conv.update({labels[i].text: info[i].text})        
    # extraer año
    info_conv.update({'anio': info_conv[u'Fecha inicio:'][:4]})
    return info_conv

def extraer_inftec(conicet_id):
    url_art = "http://www.conicet.gov.ar/new_scp/detalle.php?keywords=&id=" + str(conicet_id) + "&inf_tecnico=yes"
    response = urllib2.urlopen(url_art)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    lista = []
    for link in soup.find_all('a'):
        url = link.get('href')
        if url.startswith('detalle.php') and 'inf_tecnico_id' in url:
            url = 'http://www.conicet.gov.ar/new_scp/' + url
            lista.append(url)
    return lista   

def info_inftec(url):
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    labels = soup.find_all('div', attrs={"class": "contenido_label"})
    info = soup.find_all('div', attrs={"class": "contenido_label_info"})
    if len(labels) != len(info):
        raise IndexError('tamaños no coinciden')
    info_inftec = {}
    for i in range(len(labels)):
        info_inftec.update({labels[i].text: info[i].text})        
    # extraer año
    info_inftec.update({'anio': info_inftec[u'Fecha inicio/fin:'][:4]})
    return info_inftec


def datos_persona(id_conicet):
    # articulos
    urls = extraer_articulos(id_conicet)
    datos_arts = []
    for url in urls:
        dict_art = info_articulos(url)
        datos_arts.append(dict_art)
        time.sleep(1)
    # libros
    urls = extraer_libros(id_conicet)
    datos_lib = []
    for url in urls:
        dict_lib = info_libros(url)
        datos_lib.append(dict_lib)
        time.sleep(1)
    # capitulos
    urls = extraer_capitulos(id_conicet)
    datos_caps = []
    for url in urls:
        dict_caps = info_capitulos(url)
        datos_caps.append(dict_caps)
        time.sleep(1)
    # congresos
    urls = extraer_congresos(id_conicet)
    datos_congr = []
    for url in urls:
        dict_congr = info_congresos(url)
        datos_congr.append(dict_congr)
        time.sleep(1)
    # convenios
    urls = extraer_convenios(id_conicet)
    datos_conv = []
    for url in urls:
        dict_conv = info_convenios(url)
        datos_conv.append(dict_conv)
        time.sleep(1)
    # informe tecnico
    urls = extraer_inftec(id_conicet)
    datos_inftec = []
    for url in urls:
        dict_inftec = info_inftec(url)
        datos_inftec.append(dict_inftec)
        time.sleep(1)
    return datos_arts, datos_lib, datos_caps, datos_congr, datos_conv, datos_inftec
    
    
def transformaroutput(dictlist):
    output = defaultdict(list)
    for i in dictlist:
        output[i['anio']].append(i['Resumen:'])
    return output
    


