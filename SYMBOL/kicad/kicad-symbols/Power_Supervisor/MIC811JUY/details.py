
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Supervisor"
    oIndex = "MIC811JUY"
    hexID = "SZKPOWERSUPERVISORMIC811JUY"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MIC811LUY', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MIC811JUY', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-143', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/mic811.pdf', 'kicadSymbolki_keywords': 'Supervisor Reset', 'kicadSymbolki_description': 'Power supply supervisor, Manual reset, Threshold 4.00V, SOT-143', 'kicadSymbolki_fp_filters': 'SOT*143*'}])
    newPart['name'].append('MIC811JUY')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

