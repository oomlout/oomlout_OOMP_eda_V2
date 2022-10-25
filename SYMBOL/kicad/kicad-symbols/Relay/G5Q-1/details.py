
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "G5Q-1"
    hexID = "SZKRELAYG5Q1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'G5Q-1', 'kicadSymbolFootprint': 'Relay_THT:Relay_SPDT_Omron-G5Q-1', 'kicadSymbolDatasheet': 'https://www.omron.com/ecb/products/pdf/en-g5q.pdf', 'kicadSymbolki_keywords': 'Miniature Single Pole Relay', 'kicadSymbolki_description': 'Omron G5G relay, Miniature Single Pole, SPDT, 10A', 'kicadSymbolki_fp_filters': 'Relay*SPDT*Omron*G5Q*'}])
    newPart['name'].append('Relay : G5Q-1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

