
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "RAYEX-L90S"
    hexID = "SZKRELAYRAYEXL9S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'RAYEX-L90S', 'kicadSymbolFootprint': 'Relay_THT:Relay_SPDT_RAYEX-L90S', 'kicadSymbolDatasheet': 'https://a3.sofastcdn.com/attachment/7jioKBjnRiiSrjrjknRiwS77gwbf3zmp/L90-SERIES.pdf', 'kicadSymbolki_keywords': '30A Single Pole Relay', 'kicadSymbolki_description': 'Power relay, Without Common Terminal between coil terminals, SPDT, 30A', 'kicadSymbolki_fp_filters': 'Relay*SPDT*RAYEX*L90S*'}])
    newPart['name'].append('Relay : RAYEX-L90S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

