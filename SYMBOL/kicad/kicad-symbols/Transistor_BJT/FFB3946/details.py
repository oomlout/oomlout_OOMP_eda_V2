
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "FFB3946"
    hexID = "SZKTRANSISTORBJTFFB3946"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BC846BPN', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'FFB3946', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/FMB3946-D.pdf', 'kicadSymbolki_keywords': 'NPN/PNP Transistor', 'kicadSymbolki_description': '200mA IC, 40V Vce, Dual NPN/PNP Transistors, SOT-363', 'kicadSymbolki_fp_filters': 'SOT?363*'}])
    newPart['name'].append('Transistor_BJT : FFB3946')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

