
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BC109"
    hexID = "SZKTRANSISTORBJTBC19"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BC107', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BC109', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-18-3', 'kicadSymbolDatasheet': 'http://www.farnell.com/datasheets/296634.pdf', 'kicadSymbolki_keywords': 'NPN low noise transistor', 'kicadSymbolki_description': '0.2A Ic, 25V Vce, Low Noise General Purpose NPN Transistor, TO-18', 'kicadSymbolki_fp_filters': 'TO?18*'}])
    newPart['name'].append('Transistor_BJT : BC109')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

