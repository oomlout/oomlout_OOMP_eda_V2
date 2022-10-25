
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "NCV8402xST"
    hexID = "SZKDRIVERFETNCV842XST"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'NCV8402xST', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/NCV8402-D.PDF', 'kicadSymbolki_keywords': 'MOSFET ESD Overcurrent', 'kicadSymbolki_description': 'Self-Protected Low Side Driver with Temperature and Current Limit, SOT−223', 'kicadSymbolki_fp_filters': 'SOT?223*'}])
    newPart['name'].append('Driver_FET : NCV8402xST')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

