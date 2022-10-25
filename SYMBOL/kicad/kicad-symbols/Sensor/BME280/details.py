
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor"
    oIndex = "BME280"
    hexID = "SZKSENBME28"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BME280', 'kicadSymbolFootprint': 'Package_LGA:Bosch_LGA-8_2.5x2.5mm_P0.65mm_ClockwisePinNumbering', 'kicadSymbolDatasheet': 'https://ae-bst.resource.bosch.com/media/_tech/media/datasheets/BST-BME280-DS002.pdf', 'kicadSymbolki_keywords': 'Bosch pressure humidity temperature environment environmental measurement digital', 'kicadSymbolki_description': '3-in-1 sensor, humidity, pressure, temperature, I2C and SPI interface, 1.71-3.6V, LGA-8', 'kicadSymbolki_fp_filters': '*LGA*2.5x2.5mm*P0.65mm*Clockwise*'}])
    newPart['name'].append('Sensor : BME280')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

