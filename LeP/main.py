import utils

def main(arquivo):
    '''
    '''
    texto = utils.le_arquivos(arquivo)
    palavras = utils.tokeniza_palavras(texto)
    palavras = utils.elimina_indesejaveis(palavras)
    lexico = utils.faz_lexico(palavras)
    utils.escreve_lexico(palavras)
    return True

main([ 'textos/nome1.txt', 'textos/nome2.txt' ] )
