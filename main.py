import argparse

from core.markov import Markov
from core.parser import Parser
from core.shell  import Shell

parser = argparse.ArgumentParser(description='Cadeia de markov', add_help=False)
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Mostra essa mensagem e sai.')
parser.add_argument('-f', '--file', action='store', nargs=1, help='Arquivo HTML exportado do telegram de entrada.')

args = parser.parse_args()

if args.file :

    input_file = open(str(args.file[0]), 'r').read()

    parser = Parser(content = input_file)
    texto  = parser.parsed_content

    markov = Markov( texto, randomLimite=True )
    markov.treinar()

    shell = Shell(markov)
    shell.executar()

else :
    print('Precisa fornecer o caminho do arquivo de entrada')