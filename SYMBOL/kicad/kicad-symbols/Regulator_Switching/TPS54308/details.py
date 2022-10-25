
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS54308"
    hexID = "SZKREGULATORSWITCHINGTPS5438"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS54302', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS54308', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-6', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps54308.pdf', 'kicadSymbolki_keywords': 'switching buck converter power-supply voltage regulator emi spread spectrum FCCM', 'kicadSymbolki_description': '3A, 4.5 to 28V Input, EMI Friendly integrated switch synchronous step-down regulator, continuous-conduction, SOT-23-6', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Switching : TPS54308')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

