
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BC847BPN"
    hexID = "SZKTRANSISTORBJTBC847BPN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BC846BPN', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BC847BPN', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/BC847BPN.pdf', 'kicadSymbolki_keywords': 'NPN/PNP Transistor', 'kicadSymbolki_description': '100mA IC, 45V Vce, Dual NPN/PNP Transistors, SOT-363', 'kicadSymbolki_fp_filters': 'SOT?363*'}])
    newPart['name'].append('Transistor_BJT : BC847BPN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

