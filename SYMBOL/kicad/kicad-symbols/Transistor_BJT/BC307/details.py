
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BC307"
    hexID = "SZKTRANSISTORBJTBC37"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BC307', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub_link/Collateral/BC307-D.PDF', 'kicadSymbolki_keywords': 'Epitaxial Silicon PNP Transistor', 'kicadSymbolki_description': '100mA Ic, 45V Vce, Epitaxial Silicon PNP Transistor, TO-92', 'kicadSymbolki_fp_filters': 'TO?92*'}])
    newPart['name'].append('Transistor_BJT : BC307')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

