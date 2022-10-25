
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "FMB2227A"
    hexID = "SZKTRANSISTORBJTFMB2227A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'FMB2227A', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SuperSOT-6', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/FMB2227A-D.PDF', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'NPN/PNP Transistor', 'kicadSymbolki_description': '500mA IC, 30V Vce, Dual NPN/PNP Transistors, SuperSOT-6', 'kicadSymbolki_fp_filters': 'SuperSOT*'}])
    newPart['name'].append('Transistor_BJT : FMB2227A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

