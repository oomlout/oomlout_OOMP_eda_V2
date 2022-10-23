
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Magnetic"
    oIndex = "AH1806-W"
    hexID = "SZKSENMAGNETICAH186W"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AH1806-W', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SC-59', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/AH1806.pdf', 'kicadSymbolki_keywords': 'hall switch', 'kicadSymbolki_description': 'High Sensitivity Micropower Omnipolar Hall-Effect Switch, SC-59', 'kicadSymbolki_fp_filters': 'SC?59*'}])
    newPart['name'].append('AH1806-W')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

