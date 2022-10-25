
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BC857BDW1"
    hexID = "SZKTRANSISTORBJTBC857BDW1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BC856BS', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BC857BDW1', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub_link/Collateral/BC856BDW1T1-D.PDF', 'kicadSymbolki_keywords': 'PNP/PNP Transistor', 'kicadSymbolki_description': '100mA IC, 45V Vce, Dual PNP/PNP Transistors, SOT-363', 'kicadSymbolki_fp_filters': 'SOT?363*'}])
    newPart['name'].append('Transistor_BJT : BC857BDW1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

