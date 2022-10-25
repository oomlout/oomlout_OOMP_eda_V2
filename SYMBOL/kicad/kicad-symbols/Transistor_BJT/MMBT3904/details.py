
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "MMBT3904"
    hexID = "SZKTRANSISTORBJTBT394"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BC817', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'MMBT3904', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/2N3903-D.PDF', 'kicadSymbolki_keywords': 'NPN Transistor', 'kicadSymbolki_description': '0.2A Ic, 40V Vce, Small Signal NPN Transistor, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Transistor_BJT : MMBT3904')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

