
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LR8N8-G"
    hexID = "SZKREGULATORLINEARLR8N8G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LR8N8-G', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-89-3', 'kicadSymbolDatasheet': 'http://www.supertex.com/pdf/datasheets/LR8.pdf', 'kicadSymbolki_keywords': 'High-Voltage Regulator Adjustable Positive', 'kicadSymbolki_description': '30mA 450V High-Voltage Linear Regulator (Adjustable), SOT-89', 'kicadSymbolki_fp_filters': 'SOT*'}])
    newPart['name'].append('LR8N8-G')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

