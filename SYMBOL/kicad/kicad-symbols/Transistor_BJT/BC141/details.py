
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BC141"
    hexID = "SZKTRANSISTORBJTBC141"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '2N2219', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BC141', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-39-3', 'kicadSymbolDatasheet': 'http://www.farnell.com/datasheets/296634.pdf', 'kicadSymbolki_keywords': 'NPN Transistor', 'kicadSymbolki_description': '1A Ic, 60V Vce, NPN Transistor, TO-39', 'kicadSymbolki_fp_filters': 'TO?39*'}])
    newPart['name'].append('Transistor_BJT : BC141')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

