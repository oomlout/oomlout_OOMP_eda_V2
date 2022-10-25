
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "G6E"
    hexID = "SZKRELAYG6E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'G6E', 'kicadSymbolFootprint': 'Relay_THT:Relay_SPDT_Omron_G6E', 'kicadSymbolDatasheet': 'https://www.omron.com/ecb/products/pdf/en-g6e.pdf', 'kicadSymbolki_keywords': 'Single Pole Relay SPDT', 'kicadSymbolki_description': 'Omron Subminiature Sensitive SPDT Signal Switching Relay, Single-Side Stable', 'kicadSymbolki_fp_filters': 'Relay*SPDT*Omron*G6E*'}])
    newPart['name'].append('Relay : G6E')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

