import agendasapp
import agendasappabstract
import wordcloud
import matplotlib.pyplot as plt

def mapapalabras(conicetid, fuente='titulo'):
    if fuente == 'titulo':
        modulo = agendasapp
    elif fuente == 'resumen':
        modulo = agendasappabstract
        
    dictio = modulo.formatofinal(conicetid)
    preprocesado = modulo.preprocess(dictio)
    
    todojunto = ''
    
    for i in preprocesado:
        todojunto += ' '.join(i) + ' '
    
    woc = wordcloud.WordCloud(max_font_size = 40, relative_scaling=.5).generate(todojunto)
 
    plt.figure()
    plt.imshow(woc)
    plt.axis("off")
    plt.show()
    return todojunto
    
