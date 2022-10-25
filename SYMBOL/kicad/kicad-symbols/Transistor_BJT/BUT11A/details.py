
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BUT11A"
    hexID = "SZKTRANSISTORBJTBUT11A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BUT11', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BUT11A', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/BUT11A-D.pdf', 'kicadSymbolki_keywords': 'High Voltage Power NPN Transistor', 'kicadSymbolki_description': '5A Ic, 450V Vce, Silicon Power NPN Transistors, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Transistor_BJT : BUT11A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

