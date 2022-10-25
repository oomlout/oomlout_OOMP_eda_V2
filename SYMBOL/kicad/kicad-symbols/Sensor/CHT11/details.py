
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor"
    oIndex = "CHT11"
    hexID = "SZKSENCHT11"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'DHT11', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CHT11', 'kicadSymbolFootprint': 'Sensor:Aosong_DHT11_5.5x12.0_P2.54mm', 'kicadSymbolDatasheet': 'http://aosong.com/en/products-21.html', 'kicadSymbolki_keywords': 'Digital temperature humidity sensor', 'kicadSymbolki_description': 'Temperature and humidity module', 'kicadSymbolki_fp_filters': 'Aosong*DHT11*5.5x12.0*P2.54mm*'}])
    newPart['name'].append('Sensor : CHT11')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

