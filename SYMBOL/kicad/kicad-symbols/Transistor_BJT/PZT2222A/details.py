
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "PZT2222A"
    hexID = "SZKTRANSISTORBJTPZT2222A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'PZT2222A', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223-3_TabPin2', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/PN2222-D.PDF', 'kicadSymbolki_keywords': 'NPN General Puprose Transistor SMD', 'kicadSymbolki_description': '1A Ic, 40V Vce, NPN Transistor, General Purpose Transistor, SOT-223', 'kicadSymbolki_fp_filters': 'SOT?223*'}])
    newPart['name'].append('Transistor_BJT : PZT2222A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

