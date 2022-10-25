
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "BAT54SW"
    hexID = "SZKDIODEBAT54SW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'BAT54SW', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-323_SC-70', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/BAT54W_SER.pdf', 'kicadSymbolki_keywords': 'dual schottky diode', 'kicadSymbolki_description': 'Dual schottky barrier diode, in series, SOT-323', 'kicadSymbolki_fp_filters': 'SOT?323*'}])
    newPart['name'].append('Diode : BAT54SW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

