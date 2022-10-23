
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "CQ-2334"
    hexID = "SZKSENCURRENTCQ2334"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CQ-2063', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CQ-2334', 'kicadSymbolFootprint': 'Sensor_Current:AKM_CQ_7', 'kicadSymbolDatasheet': 'http://www.akm.com/akm/en/file/datasheet/CQ-2334.pdf', 'kicadSymbolki_keywords': 'hall effect current sensor', 'kicadSymbolki_description': 'High-Speed Small Current Sensor, Bidirectional, -54A to +54A, 40mV/A, CQ-7', 'kicadSymbolki_fp_filters': 'AKM*CQ*'}])
    newPart['name'].append('CQ-2334')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

