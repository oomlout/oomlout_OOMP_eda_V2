
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor"
    oIndex = "BME680"
    hexID = "SZKSENBME68"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BME680', 'kicadSymbolFootprint': 'Package_LGA:Bosch_LGA-8_3x3mm_P0.8mm_ClockwisePinNumbering', 'kicadSymbolDatasheet': 'https://ae-bst.resource.bosch.com/media/_tech/media/datasheets/BST-BME680-DS001.pdf', 'kicadSymbolki_keywords': 'Bosch gas pressure humidity temperature environment environmental measurement digital', 'kicadSymbolki_description': '4-in-1 sensor, gas, humidity, pressure, temperature, I2C and SPI interface, 1.71-3.6V, LGA-8', 'kicadSymbolki_fp_filters': '*LGA*3x3mm*P0.8mm*Clockwise*'}])
    newPart['name'].append('BME680')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

