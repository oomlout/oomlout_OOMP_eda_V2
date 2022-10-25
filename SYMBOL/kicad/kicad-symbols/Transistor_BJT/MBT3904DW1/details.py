
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "MBT3904DW1"
    hexID = "SZKTRANSISTORBJTMBT394DW1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BC846BS', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'MBT3904DW1', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub_link/Collateral/MBT3904DW1T1-D.PDF', 'kicadSymbolki_keywords': 'NPN/NPN Transistor', 'kicadSymbolki_description': '200mA IC, 40V Vce, Dual NPN/NPN Transistors, SOT-363', 'kicadSymbolki_fp_filters': 'SOT?363*'}])
    newPart['name'].append('Transistor_BJT : MBT3904DW1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

