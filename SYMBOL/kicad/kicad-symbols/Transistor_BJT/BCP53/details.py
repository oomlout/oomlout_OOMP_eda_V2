
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BCP53"
    hexID = "SZKTRANSISTORBJTBCP53"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PZT3906', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BCP53', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223-3_TabPin2', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub_link/Collateral/BCP53T1-D.PDF', 'kicadSymbolki_keywords': 'PNP Transistor', 'kicadSymbolki_description': '1A Ic, 80V Vce, PNP Medium Power Transistor, SOT-223', 'kicadSymbolki_fp_filters': 'SOT?223*'}])
    newPart['name'].append('Transistor_BJT : BCP53')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

