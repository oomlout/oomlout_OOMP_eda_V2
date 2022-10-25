
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "MMBD4448HTW"
    hexID = "SZKDIODEBD4448HTW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BAS16TW', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'MMBD4448HTW', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'http://www.diodes.com/datasheets/ds30153.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': 'Fast switching diode array 3 independent', 'kicadSymbolki_fp_filters': '*SOT?363*'}])
    newPart['name'].append('Diode : MMBD4448HTW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

