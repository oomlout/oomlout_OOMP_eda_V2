
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "NCP662SQ15"
    hexID = "SZKREGULATORLINEARNCP662SQ15"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCP662SQ15', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SC-82AB', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/NCP662-D.PDF', 'kicadSymbolki_keywords': 'LDO regulator voltage', 'kicadSymbolki_description': '100-mA, 12V Max. Input, Ultralow-IQ LDO, 1.5V, SC-82AB', 'kicadSymbolki_fp_filters': 'SC?82AB*'}])
    newPart['name'].append('NCP662SQ15')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

