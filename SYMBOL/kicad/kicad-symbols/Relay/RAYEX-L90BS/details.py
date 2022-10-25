
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "RAYEX-L90BS"
    hexID = "SZKRELAYRAYEXL9BS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'RAYEX-L90BS', 'kicadSymbolFootprint': 'Relay_THT:Relay_SPST_RAYEX-L90BS', 'kicadSymbolDatasheet': 'https://a3.sofastcdn.com/attachment/7jioKBjnRiiSrjrjknRiwS77gwbf3zmp/L90-SERIES.pdf', 'kicadSymbolki_keywords': '30A Single Pole Relay', 'kicadSymbolki_description': 'Power relay, Without Common Terminal between coil terminals, NC, SPST, 30A', 'kicadSymbolki_fp_filters': 'Relay*SPST*RAYEX*L90B*'}])
    newPart['name'].append('Relay : RAYEX-L90BS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

