
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "KA78M05_TO252"
    hexID = "SZKREGULATORLINEARKA78M5TO252"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM78M05_TO252', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'KA78M05_TO252', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-2', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/MC78M00-D.PDF', 'kicadSymbolki_keywords': 'Voltage Regulator 500mA Positive', 'kicadSymbolki_description': 'Positive 500mA 35V Linear Regulator, Fixed Output 5V, TO-252 (D-PAK)', 'kicadSymbolki_fp_filters': 'TO?252*'}])
    newPart['name'].append('Regulator_Linear : KA78M05_TO252')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

