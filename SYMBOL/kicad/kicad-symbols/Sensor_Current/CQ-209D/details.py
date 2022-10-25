
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "CQ-209D"
    hexID = "SZKSENCURRENTCQ29D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CQ-2092', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CQ-209D', 'kicadSymbolFootprint': 'Sensor_Current:AKM_CQ_7S', 'kicadSymbolDatasheet': 'http://www.akm.com/akm/en/file/datasheet/CQ-209D.pdf', 'kicadSymbolki_keywords': 'hall effect current sensor', 'kicadSymbolki_description': 'High-Speed Small-Sized Current Sensor, Bidirectional, -41A to +41A, 50mV/A, CQ-7S', 'kicadSymbolki_fp_filters': 'AKM*CQ*S*'}])
    newPart['name'].append('Sensor_Current : CQ-209D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

