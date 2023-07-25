'''
Regex written to extract fields from text strings.

'''
re.compile(r'(?<=\$)([A-Z]+)')

re.compile(r'(PULLBACK)')

re.compile(r'(?<= Price : .)(.+)')

re.compile(r'(\d+:\d+)(?= (?:AM|PM))')

re.compile(r'([A-Z]+)-USD\n\$(.+)\n.+\n.+\n.+\n\+(.+)\%')

re.compile(r'([A-Z]+/[A-Z]+)')

re.compile(r'([A-Z]+)\/[A-Z]+.+\n.+\n.+Price : \$(.+)\n.+Alert count : (.+)')

re.compile(r'(.+\/.+)\n.+\n.+\$(.+)\n.+:.(.+)')

re.compile(r'(.+)\%')

re.compile(r'([A-Z]+)-USD\n\$(.+)\n.+\n.+\n.+\n\+(.+)\%')

re.compile(r'(?<=Ticker: .)([A-Z]+)')

re.compile(r'(?<= Alert Count :)(..)')

re.compile(r'(?<= Price : .)(.....)')

re.compile(r'(?<=T)(\d+:\d+)')

re.compile(r'1\n([A-Z]+)')

re.compile(r'(.+\n)(.+)\%')

re.compile(r'20\n([A-Z]+)')

re.compile(r'(.+\n)(.+)\%')

re.compile(r'40\n([A-Z]+)')

re.compile(r'(.+)\%')

re.compile(r'([A-Z]+)\/USDT')

 re.compile(r'(?: Alert Count : )(.+)')

 re.compile(r'([A-Z]+/[A-Z]+)')

 re.compile(r'([A-Z]+)\n(.+)\%')

 re.compile(r'\$([A-Z]+)\n.+\n.+\n.+(?:Alert Count : )(.+)')