from core.markov import Markov

class Shell :
    def __init__ ( self, markov : Markov ) :
        self.markov = markov
    
    def executar ( self ) :
        if self.markov == None :
            raise Exception("Passe um objeto do tipo markov")
        while True :
            try :
                text = input ('> ')
                print(self.markov.gerar())
            except KeyboardInterrupt :
                print('\n(ง ͠° ͟ʖ ͡°)ง')
                break

        print('Execução terminada')