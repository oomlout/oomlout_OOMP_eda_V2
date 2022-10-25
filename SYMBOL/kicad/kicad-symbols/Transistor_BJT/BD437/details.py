
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BD437"
    hexID = "SZKTRANSISTORBJTBD437"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BD433', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BD437', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-126-3_Vertical', 'kicadSymbolDatasheet': 'http://www.cdil.com/datasheets/bd433_42.pdf', 'kicadSymbolki_keywords': 'Power NPN Transistor', 'kicadSymbolki_description': '4A Ic, 45V Vce, Power NPN Transistor, TO-126', 'kicadSymbolki_fp_filters': 'TO?126*'}])
    newPart['name'].append('Transistor_BJT : BD437')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

