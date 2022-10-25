
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "NCP718xSN300"
    hexID = "SZKREGULATORLINEARNCP718XSN3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LP5907MFX-1.2', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCP718xSN300', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/NCP718-D.PDF', 'kicadSymbolki_keywords': 'Single Output LDO Wide Input', 'kicadSymbolki_description': '300-mA, Wide Input Voltage, Low-IQ LDO, 3.0V, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Linear : NCP718xSN300')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

