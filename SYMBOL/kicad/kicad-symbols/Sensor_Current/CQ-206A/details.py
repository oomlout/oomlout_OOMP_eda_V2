
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "CQ-206A"
    hexID = "SZKSENCURRENTCQ26A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CQ-2063', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CQ-206A', 'kicadSymbolFootprint': 'Sensor_Current:AKM_CQ_7', 'kicadSymbolDatasheet': 'http://www.akm.com/akm/en/file/datasheet/CQ-206A.pdf', 'kicadSymbolki_keywords': 'hall effect current sensor', 'kicadSymbolki_description': 'High-Speed Small-Sized Current Sensor, Bidirectional, -46A to +46A, 45mV/A, CQ-7', 'kicadSymbolki_fp_filters': 'AKM*CQ*'}])
    newPart['name'].append('CQ-206A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

