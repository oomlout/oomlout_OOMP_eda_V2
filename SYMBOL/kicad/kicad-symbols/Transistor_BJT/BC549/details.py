
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BC549"
    hexID = "SZKTRANSISTORBJTBC549"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BC547', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BC549', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/BC550-D.pdf', 'kicadSymbolki_keywords': 'NPN Transistor', 'kicadSymbolki_description': '0.1A Ic, 30V Vce, Small Signal NPN Transistor, TO-92', 'kicadSymbolki_fp_filters': 'TO?92*'}])
    newPart['name'].append('Transistor_BJT : BC549')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

