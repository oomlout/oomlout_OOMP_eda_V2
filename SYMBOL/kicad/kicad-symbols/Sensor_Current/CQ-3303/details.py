
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "CQ-3303"
    hexID = "SZKSENCURRENTCQ333"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CQ-3200', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CQ-3303', 'kicadSymbolFootprint': 'Sensor_Current:AKM_CQ_VSOP-24_5.6x7.9mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.akm.com/akm/en/file/datasheet/CQ-3303.pdf', 'kicadSymbolki_keywords': 'hall effect current sensor', 'kicadSymbolki_description': 'High-Speed Response Coreless Current Sensor, Bidirectional, -35.0A to +35.0A, 60mV/A, VSOP-24', 'kicadSymbolki_fp_filters': 'AKM*CQ*VSOP*5.6x7.9mm*P0.65mm*'}])
    newPart['name'].append('CQ-3303')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

