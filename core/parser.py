from bs4 import BeautifulSoup

class Parser :

    def __init__ ( self, content : str = '' ) :
        self.content = content
        self.parsed_content = []
        if self.content != '' :
            self.parsed_content = self.__treinar()

    def __treinar ( self ) :
        soup = BeautifulSoup(self.content, 'html.parser')
        parsed = soup.findAll('div', { "class" : "text" })[1:]
        string_parsed = ''.join(str(i.text) + ' ' for i in parsed if 'http' not in i.text)
        a = string_parsed.split(' ')
        a = [ item.strip(' ').strip('\n').strip('\t').lower() for item in a if item != '']
        return ' '.join([ s for s in a ])