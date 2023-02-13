import re
sentence = 'horses are fast'
regex = re.compile('(?P<animal>w+) (?P<verb>w+) (?P<adjective>w+)')
matched = re.search(regex, sentence)
print(matched.groupdict())
