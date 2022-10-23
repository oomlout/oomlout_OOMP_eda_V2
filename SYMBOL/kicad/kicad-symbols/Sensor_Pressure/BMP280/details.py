
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Pressure"
    oIndex = "BMP280"
    hexID = "SZKSENPRESSUREBMP28"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BMP280', 'kicadSymbolFootprint': 'Package_LGA:Bosch_LGA-8_2x2.5mm_P0.65mm_ClockwisePinNumbering', 'kicadSymbolDatasheet': 'https://ae-bst.resource.bosch.com/media/_tech/media/datasheets/BST-BMP280-DS001.pdf', 'kicadSymbolki_keywords': 'I2C, SPI, pressure, temperature, sensor', 'kicadSymbolki_description': 'Absolute Barometric Pressure Sensor, LGA-8', 'kicadSymbolki_fp_filters': 'Bosch*LGA*2x2.5mm*P0.65mm*'}])
    newPart['name'].append('BMP280')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

