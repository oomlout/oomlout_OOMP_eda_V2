
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "CQ-209B"
    hexID = "SZKSENCURRENTCQ29B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CQ-2092', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CQ-209B', 'kicadSymbolFootprint': 'Sensor_Current:AKM_CQ_7S', 'kicadSymbolDatasheet': 'http://www.akm.com/akm/en/file/datasheet/CQ-209B.pdf', 'kicadSymbolki_keywords': 'hall effect current sensor', 'kicadSymbolki_description': 'High-Speed Small-Sized Current Sensor, Unidirectional, -35A to 0A, 115mV/A, CQ-7S', 'kicadSymbolki_fp_filters': 'AKM*CQ*S*'}])
    newPart['name'].append('Sensor_Current : CQ-209B')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

