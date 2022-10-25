
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "PZTA92"
    hexID = "SZKTRANSISTORBJTPZTA92"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'PZTA92', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223-3_TabPin2', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/PZTA92T1-D.PDF', 'kicadSymbolki_keywords': 'PNP High Voltage Transistor', 'kicadSymbolki_description': '0.5A Ic, 300V Vce, PNP High Voltage Transistor, SOT-223', 'kicadSymbolki_fp_filters': 'SOT?223*'}])
    newPart['name'].append('Transistor_BJT : PZTA92')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

