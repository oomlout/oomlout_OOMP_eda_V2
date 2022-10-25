
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BD436"
    hexID = "SZKTRANSISTORBJTBD436"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BD434', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BD436', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-126-3_Vertical', 'kicadSymbolDatasheet': 'http://www.cdil.com/datasheets/bd433_42.pdf', 'kicadSymbolki_keywords': 'Power PNP Transistor', 'kicadSymbolki_description': '4A Ic, 32V Vce, Power PNP Transistor, TO-126', 'kicadSymbolki_fp_filters': 'TO?126*'}])
    newPart['name'].append('Transistor_BJT : BD436')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

