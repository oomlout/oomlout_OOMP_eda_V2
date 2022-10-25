
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MC79M15_TO252"
    hexID = "SZKREGULATORLINEARMC79M15TO252"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MC79M05_TO252', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MC79M15_TO252', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-2', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/MC79M00-D.PDF', 'kicadSymbolki_keywords': 'Voltage Regulator 500mA Negative', 'kicadSymbolki_description': 'Negative 500mA 35V Linear Regulator, Fixed Output -15V, TO-252', 'kicadSymbolki_fp_filters': 'TO?252*'}])
    newPart['name'].append('Regulator_Linear : MC79M15_TO252')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

