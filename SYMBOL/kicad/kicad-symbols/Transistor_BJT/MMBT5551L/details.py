
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "MMBT5551L"
    hexID = "SZKTRANSISTORBJTBT5551L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BC817', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'MMBT5551L', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'www.onsemi.com/pub/Collateral/MMBT5550LT1-D.PDF', 'kicadSymbolki_keywords': 'NPN Transistor', 'kicadSymbolki_description': '0.6A Ic, 160V Vce, NPN Transistor, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Transistor_BJT : MMBT5551L')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

