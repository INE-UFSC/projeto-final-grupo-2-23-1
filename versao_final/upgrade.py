from ler_txt import LerTXT

class Upgrade:
    def __init__(self, jogo):
        self.__jogo = jogo
        self.__dicionario_upgrades = self.ler_upgrade()

    def aplicar_upgrade(self, text_selecionado):
        chave = self.__dicionario_upgrades[text_selecionado]
        
        for i in range(len(chave)):
            chaves = chave[i].keys()
            if 'dano' in chaves:
                self.dano(chave[i]['dano'])
            elif 'vida' in chaves:
                self.vida(chave[i]['vida'])
            elif 'pulo' in chaves:
                self.pulo(chave[i]['pulo'])
            elif 'velocidade' in chaves:
                self.velocidade(chave[i]['velocidade'])
            elif 'velocidadeatk' in chaves:
                self.velocidadeatk(chave[i]['velocidadeatk'])
    
    def ler_upgrade(self):
        palavras = []
        listanomes = [] 
        ler = LerTXT()
        
        listanomes.append(ler.ler('cartas.txt'))
        listanomes.append(ler.ler('cartas_inc.txt'))
    
        for i in range(2):
            for frase in listanomes[i]:
                palavras.extend(frase.split())
            
        dicionario = {}
        for i in range(0, len(palavras)):
            try:
                if 'png' in palavras[i]:
                    chave = palavras[i][:-4]
                    dicionario[chave] = []
                    while True:
                        valor_chave = palavras[i + 1]
                        valor = palavras[i + 2]
                        dicionario[chave].append({valor_chave: valor})
                        if 'png' in palavras[i+3]:
                            break
                        else:
                            i += 2 
            except IndexError:
                continue

        return dicionario
    
    def dano(self, valor):
        if valor[0] == 'a':
            self.__jogo.jogador.arma.tipo_projetil.dano += int(self.__jogo.jogador.arma.tipo_projetil.dano * float(valor[3:]))
        elif valor[0] == 's':
            self.__jogo.jogador.arma.tipo_projetil.dano -= int(self.__jogo.jogador.arma.tipo_projetil.dano * float(valor[4:]))
        elif valor[0] == '+':
            self.__jogo.jogador.arma.tipo_projetil.dano += int(float(valor[1:]))
        elif valor[0] == '-':
            self.__jogo.jogador.arma.tipo_projetil.dano -= int(float(valor[1:]))

    def vida(self, valor):
        if valor[0] == 'a':
            self.__jogo.jogador.vida_total += int(self.__jogo.jogador.vida_total  * float(valor[3:]))
        elif valor[0] == 's':
            self.__jogo.jogador.vida_total -= int(self.__jogo.jogador.vida_total  * float(valor[4:]))
        elif valor[0] == '+':
            self.__jogo.jogador.vida_total += int(float(valor[1:]))
        elif valor[0] == '-':
            self.__jogo.jogador.vida_total -= int(float(valor[1:]))

        self.__jogo.jogador.vida_atual = self.__jogo.jogador.vida_total

    def pulo(self, valor):
        if valor[0] == 'a':
            self.__jogo.jogador.ALTURA_PULO += int(self.__jogo.jogador.ALTURA_PULO  * float(valor[3:]))
        elif valor[0] == 's':
            self.__jogo.jogador.ALTURA_PULO -= int(self.__jogo.jogador.ALTURA_PULO  * float(valor[4:]))
        elif valor[0] == '+':
            self.__jogo.jogador.ALTURA_PULO += int(float(valor[1:]))
        elif valor[0] == '-':
            self.__jogo.jogador.ALTURA_PULO -= int(float(valor[1:]))

    def velocidade(self,valor):
        if valor[0] == 'a':
            self.__jogo.jogador.veloc_mov += int(self.__jogo.jogador.veloc_mov  * float(valor[3:]))
        elif valor[0] == 's':
            self.__jogo.jogador.veloc_mov -= int(self.__jogo.jogador.veloc_mov  * float(valor[4:]))
        elif valor[0] == '+':
            self.__jogo.jogador.veloc_mov += int(float(valor[1:]))
        elif valor[0] == '-':
            self.__jogo.jogador.veloc_mov -= int(float(valor[1:]))

    def velocidadeatk(self,valor):
        if valor[0] == 'a':
            self.__jogo.jogador.arma.TEMPO_RECARGA += int(self.__jogo.jogador.arma.TEMPO_RECARGA  * float(valor[3:]))
        elif valor[0] == 's':
            self.__jogo.jogador.arma.TEMPO_RECARGA -= int(self.__jogo.jogador.arma.TEMPO_RECARGA  * float(valor[4:]))
        elif valor[0] == '+':
            self.__jogo.jogador.arma.TEMPO_RECARGA += int(float(valor[1:]))
        elif valor[0] == '-':
            self.__jogo.jogador.arma.TEMPO_RECARGA -= int(float(valor[1:]))
