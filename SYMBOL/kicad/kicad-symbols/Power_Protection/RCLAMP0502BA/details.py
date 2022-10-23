
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "RCLAMP0502BA"
    hexID = "SZKPOWERPROTECTIONRCLAMP52BA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'RCLAMP0502B', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'RCLAMP0502BA', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-416', 'kicadSymbolDatasheet': 'https://www.semtech.com/products/circuit-protection/low-capacitance/rclamp0502ba', 'kicadSymbolki_keywords': 'tvs unidirectional', 'kicadSymbolki_description': 'Low capacitance unidirectional dual ESD protection diode, SC-75', 'kicadSymbolki_fp_filters': 'SOT?416*'}])
    newPart['name'].append('RCLAMP0502BA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

