
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BC160"
    hexID = "SZKTRANSISTORBJTBC16"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BC160', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-39-3', 'kicadSymbolDatasheet': 'http://www.farnell.com/datasheets/1697389.pdf', 'kicadSymbolki_keywords': 'power PNP Transistor', 'kicadSymbolki_description': '1A Ic, 40V Vce, Power PNP Transistor, TO-39', 'kicadSymbolki_fp_filters': 'TO?39*'}])
    newPart['name'].append('Transistor_BJT : BC160')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

