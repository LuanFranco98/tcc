
from bs4 import BeautifulSoup
    
def getParsedHtmlWithIds(filename):
    with open(filename) as f:
        file = f.read()
    parsed_html = BeautifulSoup(file)
    return parsed_html

def getIdsFromParsedHtml(parsed_html):
    ids = []
    for div in parsed_html.findAll('div'):
        ids.append(div.get('data-appid'))
    return ids

def writeIdsToFile(ids):
    with open('ids.txt', 'w') as f:
        for id in ids:
            f.write(id + '\n')
    print('Done')


def __main__():
    parsedHtml = getParsedHtmlWithIds('list.txt')
    ids = getIdsFromParsedHtml(parsedHtml)
    writeIdsToFile(ids)
    return

__main__()