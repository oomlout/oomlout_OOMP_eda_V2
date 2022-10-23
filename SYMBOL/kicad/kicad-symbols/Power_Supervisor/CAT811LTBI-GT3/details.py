
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Supervisor"
    oIndex = "CAT811LTBI-GT3"
    hexID = "SZKPOWERSUPERVISORCAT811LTBIGT3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MIC811LUY', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CAT811LTBI-GT3', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-143', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/CAT811-D.PDF', 'kicadSymbolki_keywords': 'Supervisor Reset', 'kicadSymbolki_description': 'Power supply supervisor, Manual reset, Threshold 4.63V, SOT-143', 'kicadSymbolki_fp_filters': 'SOT*143*'}])
    newPart['name'].append('CAT811LTBI-GT3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

