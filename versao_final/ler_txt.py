import os
class LerTXT:
    def __init__(self):
        self.__listanomes = []
        self.__diretorio_atual = os.chdir(os.path.dirname(__file__))
        
    
    def ler(self, nome_arquivo):
        self.__listanomes = []
        with open(os.path.join('txts', nome_arquivo), "r") as arquivo:
            conteudo = arquivo.read()
            self.__listanomes.append(conteudo.splitlines())
        palavras = []
        for frase in self.__listanomes[0]:
            palavras.extend(frase.split())
        return palavras

