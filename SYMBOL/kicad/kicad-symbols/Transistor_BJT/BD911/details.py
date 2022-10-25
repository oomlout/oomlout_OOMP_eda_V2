
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BD911"
    hexID = "SZKTRANSISTORBJTBD911"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BD911', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'http://www.st.com/internet/com/TECHNICAL_RESOURCES/TECHNICAL_LITERATURE/DATASHEET/CD00001277.pdf', 'kicadSymbolki_keywords': 'Power NPN Transistor', 'kicadSymbolki_description': '15A, Silicon Power NPN Transistors, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Transistor_BJT : BD911')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

