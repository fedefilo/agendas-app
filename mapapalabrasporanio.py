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
    
    
    
    for i in range(len(preprocesado)):
        todojunto = ''
        todojunto += ' '.join(preprocesado[i]) + ' '
        woc = wordcloud.WordCloud(max_font_size = 40, relative_scaling=.5).generate(todojunto)        
        plt.figure()
        plt.suptitle(str(dictio.keys()[i]))
        plt.imshow(woc)
        plt.axis("off")
        plt.savefig(str(dictio.keys()[i]) + '.png')
        plt.show()
       
 #   
 #   woc = wordcloud.WordCloud(max_font_size = 40, relative_scaling=.5).generate(todojunto)
 #
 #   plt.figure()
 #   plt.imshow(woc)
 #   plt.axis("off")
 #   plt.show()
 #   return todojunto
 #   
