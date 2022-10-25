
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "KA378R05"
    hexID = "SZKREGULATORLINEARKA378R5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'KA378R05', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-4_Vertical', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/KA378R05-D.pdf', 'kicadSymbolki_keywords': 'Voltage Regulator 3A Positive LDO Disable Pin', 'kicadSymbolki_description': 'Positive 3A 35V Linear Regulator with Disable Pin, LDO, Fixed Output 5V, TO-220F-4L', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Regulator_Linear : KA378R05')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

