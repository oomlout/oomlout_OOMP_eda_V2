
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "MMBF4393"
    hexID = "SZKTRANSISTORFETBF4393"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BSR56', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'MMBF4393', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/MMBF4391LT1-D.PDF', 'kicadSymbolki_keywords': 'N-Channel FET Transistor', 'kicadSymbolki_description': '5mA min, 30V, 100mOhm max, 0.5-3V Vgs(off), N-Channel JFET, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Transistor_FET : MMBF4393')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

