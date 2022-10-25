
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BC818W"
    hexID = "SZKTRANSISTORBJTBC818W"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BC817W', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BC818W', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-323_SC-70', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/BC818-D.pdf', 'kicadSymbolki_keywords': 'NPN Transistor', 'kicadSymbolki_description': '0.8A Ic, 25V Vce, NPN Transistor, SOT-323', 'kicadSymbolki_fp_filters': 'SOT?323*'}])
    newPart['name'].append('Transistor_BJT : BC818W')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

