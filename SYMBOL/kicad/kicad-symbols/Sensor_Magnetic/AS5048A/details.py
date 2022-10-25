
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Magnetic"
    oIndex = "AS5048A"
    hexID = "SZKSENMAGNETICAS548A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AS5048A', 'kicadSymbolFootprint': 'Package_SO:TSSOP-14_4.4x5mm_P0.65mm', 'kicadSymbolDatasheet': 'https://ams.com/documents/20143/36005/AS5048_DS000298_4-00.pdf', 'kicadSymbolki_keywords': 'sensor magnetic hall position rotation spi', 'kicadSymbolki_description': 'Magnetic position sensor, 14-bit, PWM output, SPI Interface, TSSOP-14', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('Sensor_Magnetic : AS5048A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

