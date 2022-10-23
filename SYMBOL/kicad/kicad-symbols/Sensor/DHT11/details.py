
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor"
    oIndex = "DHT11"
    hexID = "SZKSENDHT11"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DHT11', 'kicadSymbolFootprint': 'Sensor:Aosong_DHT11_5.5x12.0_P2.54mm', 'kicadSymbolDatasheet': 'http://akizukidenshi.com/download/ds/aosong/DHT11.pdf', 'kicadSymbolki_keywords': 'Digital temperature humidity sensor', 'kicadSymbolki_description': 'Temperature and humidity module', 'kicadSymbolki_fp_filters': 'Aosong*DHT11*5.5x12.0*P2.54mm*'}])
    newPart['name'].append('DHT11')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

