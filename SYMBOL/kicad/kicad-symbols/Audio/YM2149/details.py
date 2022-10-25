
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "YM2149"
    hexID = "SZKAUDIOYM2149"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'YM2149', 'kicadSymbolFootprint': 'Package_DIP:DIP-40_W15.24mm', 'kicadSymbolDatasheet': 'http://www.ym2149.com/ym2149.pdf', 'kicadSymbolki_keywords': 'audio ssg 3ch', 'kicadSymbolki_description': 'Software-Controlled Sound Generator, DIP-40', 'kicadSymbolki_fp_filters': 'DIP*W15.24mm*'}])
    newPart['name'].append('Audio : YM2149')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

