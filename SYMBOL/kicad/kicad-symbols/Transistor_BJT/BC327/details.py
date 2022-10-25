
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BC327"
    hexID = "SZKTRANSISTORBJTBC327"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BC557', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BC327', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub_link/Collateral/BC327-D.PDF', 'kicadSymbolki_keywords': 'PNP Transistor', 'kicadSymbolki_description': '0.8A Ic, 45V Vce, PNP Transistor, TO-92', 'kicadSymbolki_fp_filters': 'TO?92*'}])
    newPart['name'].append('Transistor_BJT : BC327')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

