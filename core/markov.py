import random as rnd

class Markov :

    def __init__ ( self, text : str = '', limite : int = 50, randomLimite = False ) :
        self.text = text
        self.dictionary = {}
        self.dict_keys  = []
        self.limite = limite
        self.randomLimite = randomLimite

    def treinar ( self ) :
        if self.text in ( None, '' ) :
            raise Exception('Para treinar, precisa-se fornecer uma string')
        
        splited_text = self.text.lower().split(' ')

        for i in range ( 0, len(splited_text) - 2 ) :
            key = f"{splited_text[i]} {splited_text[i + 1]}"
            if key not in self.dictionary :
                self.dictionary[key] = [ splited_text[i + 2] ]
            else :
                self.dictionary[key].append(splited_text[i + 2])
        
        self.dict_keys = list(self.dictionary)

    def gerar ( self ) :
        texto_gerado = ''
        count = 0

        if self.dictionary == {} :
            raise Exception('Para gerar texto, precisa-se treinar')

        i = rnd.choice(range(0, len(self.dict_keys) - 1))

        lim = self.limite
        
        if self.randomLimite :
            lim = 8 + rnd.randint(0, 100)

        while count < lim and i < len(self.dict_keys) :
            words          = self.dictionary[ self.dict_keys[i] ]
            word           = rnd.choice(words)
            texto_gerado  += word + ' '
            i              = ( i + 1 ) % len(self.dict_keys)
            count         += 1

        return texto_gerado
        
        
