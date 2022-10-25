
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "MMDT5401"
    hexID = "SZKTRANSISTORBJTDT541"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BC856BS', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'MMDT5401', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'http://www.diodes.com/_files/datasheets/ds30169.pdf', 'kicadSymbolki_keywords': 'PNP/PNP Transistor', 'kicadSymbolki_description': '200mA IC, 160V Vce, Dual PNP/PNP Transistors, SOT-363', 'kicadSymbolki_fp_filters': 'SOT?363*'}])
    newPart['name'].append('Transistor_BJT : MMDT5401')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

