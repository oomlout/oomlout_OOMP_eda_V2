
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "BAT54A"
    hexID = "SZKDIODEBAT54A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'BAT54A', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'http://www.diodes.com/_files/datasheets/ds11005.pdf', 'kicadSymbolki_keywords': 'schottky diode', 'kicadSymbolki_description': 'schottky barrier diode', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Diode : BAT54A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

