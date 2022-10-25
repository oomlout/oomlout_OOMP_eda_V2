
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "CQ-206B"
    hexID = "SZKSENCURRENTCQ26B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CQ-2063', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CQ-206B', 'kicadSymbolFootprint': 'Sensor_Current:AKM_CQ_7', 'kicadSymbolDatasheet': 'http://www.akm.com/akm/en/file/datasheet/CQ-206B.pdf', 'kicadSymbolki_keywords': 'hall effect current sensor', 'kicadSymbolki_description': 'High-Speed Small-Sized Current Sensor, Unidirectional, 0A to +45A, 90mV/A, CQ-7', 'kicadSymbolki_fp_filters': 'AKM*CQ*'}])
    newPart['name'].append('Sensor_Current : CQ-206B')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

