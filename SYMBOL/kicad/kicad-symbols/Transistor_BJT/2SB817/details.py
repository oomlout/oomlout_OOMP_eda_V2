
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "2SB817"
    hexID = "SZKTRANSISTORBJT2SB817"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': '2SB817', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-3PB-3_Vertical', 'kicadSymbolDatasheet': 'http://skory.gylcomp.hu/alkatresz/2SB817.pdf', 'kicadSymbolki_keywords': 'Power PNP Transistor', 'kicadSymbolki_description': '-12A Ic, -140V Vce, Silicon Power PNP Transistors, TO-3PB', 'kicadSymbolki_fp_filters': 'TO?3PB*'}])
    newPart['name'].append('2SB817')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

