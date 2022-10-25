
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Gas"
    oIndex = "MQ-6"
    hexID = "SZKSENGASMQ6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MQ-6', 'kicadSymbolFootprint': 'Sensor:MQ-6', 'kicadSymbolDatasheet': 'https://www.winsen-sensor.com/d/files/semiconductor/mq-6.pdf', 'kicadSymbolki_keywords': 'flammable gas sensor LPG', 'kicadSymbolki_description': 'Semiconductor Sensor for Flammable Gas', 'kicadSymbolki_fp_filters': '*MQ*6*'}])
    newPart['name'].append('Sensor_Gas : MQ-6')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

