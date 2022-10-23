
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Magnetic"
    oIndex = "AH1806-Z"
    hexID = "SZKSENMAGNETICAH186Z"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AH1806-Z', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-553', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/AH1806.pdf', 'kicadSymbolki_keywords': 'hall switch', 'kicadSymbolki_description': 'High Sensitivity Micropower Omnipolar Hall-Effect Switch, SOT-553', 'kicadSymbolki_fp_filters': 'SOT*553*'}])
    newPart['name'].append('AH1806-Z')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

