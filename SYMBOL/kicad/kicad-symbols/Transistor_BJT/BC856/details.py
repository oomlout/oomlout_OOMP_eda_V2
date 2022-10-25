
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BC856"
    hexID = "SZKTRANSISTORBJTBC856"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BC807', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BC856', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/BC860-D.pdf', 'kicadSymbolki_keywords': 'PNP transistor', 'kicadSymbolki_description': '0.1A Ic, 65V Vce, PNP Transistor, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Transistor_BJT : BC856')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

