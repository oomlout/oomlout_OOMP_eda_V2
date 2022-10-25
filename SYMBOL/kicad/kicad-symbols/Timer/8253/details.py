
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer"
    oIndex = "8253"
    hexID = "SZKTIMER8253"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '82C54', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '8253', 'kicadSymbolFootprint': 'Package_DIP:DIP-24_W15.24mm', 'kicadSymbolDatasheet': 'http://www.cpcwiki.eu/imgs/e/e3/8253.pdf', 'kicadSymbolki_keywords': 'Timer Counter', 'kicadSymbolki_description': 'Programmable Interval Timer, PDIP-24', 'kicadSymbolki_fp_filters': 'DIP*W15.24mm*'}])
    newPart['name'].append('Timer : 8253')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

