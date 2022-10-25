
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "BAT54ADW"
    hexID = "SZKDIODEBAT54ADW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'BAT54ADW', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'http://www.diodes.com/datasheets/ds30152.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': 'Schottky diode array 2 pair Com A', 'kicadSymbolki_fp_filters': 'SOT?363*'}])
    newPart['name'].append('Diode : BAT54ADW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

