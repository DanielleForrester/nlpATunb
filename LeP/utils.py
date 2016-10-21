# -*- coding: cp1252 -*-
#le arq
INDESEJAVEIS = '. , ; : ! ? ) ] "'.split()
ALFABETO = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()

def le_arquivos(arquivos):
    '''
    le varios arquivos, retorna conteudo como string
    
    :param arquivos : uma lista de endereços de arquivos
    '''
    conteudo = ''
    for arquivo in arquivos:
        conteudo = conteudo + le_arquivo(arquivo) + ' '
    return conteudo

def le_arquivo(arquivo):
    arq = open(arquivo, 'r')
    conteudo = arq.read()
    arq.close()
    return conteudo

def tokeniza_palavras(texto):
    '''
    retorna lista de strings (palavras do texto)

    :param texto: string
    '''
    return texto.split()

def elimina_indesejaveis(palavras):
    '''
    retorna lista palavras sem itens terminados em indesejaveis
    
    substitui palavras da lista palavras que terminem em um dos
    simbolos indesejaveis pela mesma palavra menos o simbolo indesejavel
    Obs: não elimina palavaras da lista!

    :param palavras: lista de strings

    '''
    for i, palavra in enumerate(palavras):
        palavras[i] = elimina_indesejavel(palavra)
        
def elimina_indesejavel(palavra):
    '''
    retorna palavra eliminando simbolo não alfabetico a sua direita se houver
    '''
    for indesejavel in INDESEJAVEIS:
        if indesejavel in palavra: palavra = palavra[:-1]
        else: continue
    return palavra


def faz_lexico(palavras):
    '''
    retorna lexico --> lista de palavras em ordem alfabetica sem repetiçoes
    e sem maiusculas

    :param palavras: lista de strings
    '''
    lexico = []
    for palavra in palavras:
        palavra = palavra.lower()
        if palavra in lexico: continue
        else: lexico.append(palavra)
    lexico.sort()
    return lexico

def 
