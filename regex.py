'''
Regex written to extract fields from text strings.

'''
re.compile(r'([A-Z]+)USD\n')

re.compile(r'((.+)\%')

re.compile(r'([A-Z]+)USD')

re.compile(r'([A-Z]+)USD(?:.|\n)')

re.compile(r'([A-Z]+)USD\n')

re.compile(r'([A-Z]+)USD')

re.compile(r'([A-Z]+)USD(?:.|\n)')

re.compile(r'(.+\n)(.+)\%')

re.compile(r'([A-Z]+)\n')

re.compile(r'([A-Z]+)(?:(.|\n)+)([0-9]+\.[0-9]+)\n([0-9]+\.[0-9]+)\%')

re.compile(r'(.+\/.+)\n.+\n.+\$(.+)\n.+:.(.+)')

re.compile(r'(.+\/.+)\n.(PULLBACK|.+)\n.+\$(.+)\n.+:.(.+)')

re.compile(r'\$(.+)\n.(PULLBACK|.+)\n.+\$(.+)\n.+:.(.+)')

re.compile(r'\$(.+)\n.(PULLBACK|.+\n).Price.\$(.+)\n.+:.(.+)')

re.compile(r'\$(.+)\n.(PULLBACK|.+\n).Price.\$(.+)\n.(Alert Count :.(.+)|.+\n)')

re.compile(r'\$([A-Z]+)\n.+\n.+\n.+(?:.Alert Count.:.)(.+)')

re.compile(r'\$([A-Z]+)\n.+\n.+\n.+(?: Alert Count : )(.+)')

re.compile(r'\$(?P<coin>[A-Z]+)\n.+\n.+(?:\$)(?P<price>.+)\n.+(?: )(?P<ac>.+)')

re.compile(r'\$(?P<coin>[A-Z]+)\n.+\n.(?: Price : \$)(?P<price>.+)\n.+(?: )(?P<ac>.+)')

re.compile(r'(?P<coin> [A-Z]+\/[A-Z]+).+\n.+\n.+\n.+(?: Alert count : )(?P<ac>.+)')

re.compile(r'(?P<ticker>[A-Z]+\/[A-Z]+)\n(?: Price: .)(?P<price>.+)\n(?: Alert Count: )(?P<ac>.+)')

re.compile(r'?P<ticker>[A-Z]+)\n(?: Price: .)(?P<price>.+)\n(?: Alert Count: )(?P<ac>.+)')

re.compile(r'[A-Z]+)\n(?: Price: .)(.+)\n(?: Alert Count: )(.+)')

re.compile(r'[A-Z]+\/[A-Z]+)\n(?: Price: .)(.+)\n(?: Alert count: )(.+)')

re.compile(r'(?<=\$)([A-Z]+)')

re.compile(r'(11/../2022 .... ..)')

re.compile(r'(?<=Alert Count :)(.+)')

re.compile(r'(?<= Price : .)(.+)')

re.compile(r'(\d+:\d+)(?= (?:AM|PM))')

re.compile(r'(?<=T)(\d+:\d+)')

re.compile(r'(PULLBACK)')

re.compile(r'([A-Z]+/[A-Z]+)')

re.compile(r'(\$)(.+)')

re.compile(r'(?:\$| Alert Count : )(.+)')
