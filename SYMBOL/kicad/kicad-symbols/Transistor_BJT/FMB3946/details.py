
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "FMB3946"
    hexID = "SZKTRANSISTORBJTFMB3946"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FMB2227A', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'FMB3946', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SuperSOT-6', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/FMB3946-D.pdf', 'kicadSymbolki_keywords': 'NPN/PNP Transistor', 'kicadSymbolki_description': '200mA IC, 40V Vce, Dual NPN/PNP Transistors, SuperSOT-6', 'kicadSymbolki_fp_filters': 'SuperSOT*'}])
    newPart['name'].append('Transistor_BJT : FMB3946')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

