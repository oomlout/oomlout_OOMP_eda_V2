
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "NCP1117-1.5_SOT223"
    hexID = "SZKREGULATORLINEARNCP111715SOT223"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AP1117-15', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCP1117-1.5_SOT223', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223-3_TabPin2', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub_link/Collateral/NCP1117-D.PDF', 'kicadSymbolki_keywords': 'REGULATOR LDO 1.5V', 'kicadSymbolki_description': '1A Low drop-out regulator, Fixed Output 1.5V, SOT-223', 'kicadSymbolki_fp_filters': 'SOT?223*TabPin2*'}])
    newPart['name'].append('Regulator_Linear : NCP1117-1.5_SOT223')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

