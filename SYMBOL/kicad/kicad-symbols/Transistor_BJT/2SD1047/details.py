
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "2SD1047"
    hexID = "SZKTRANSISTORBJT2SD147"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': '2SD1047', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-3PB-3_Vertical', 'kicadSymbolDatasheet': 'http://www.st.com/resource/en/datasheet/2sd1047.pdf', 'kicadSymbolki_keywords': 'Power NPN Transistor', 'kicadSymbolki_description': '12A Ic, 140V Vce, Silicon Power NPN Transistors, TO-3PB', 'kicadSymbolki_fp_filters': 'TO?3PB*'}])
    newPart['name'].append('Transistor_BJT : 2SD1047')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

