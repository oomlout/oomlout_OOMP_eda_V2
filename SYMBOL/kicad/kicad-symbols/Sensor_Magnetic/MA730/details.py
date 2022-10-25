
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Magnetic"
    oIndex = "MA730"
    hexID = "SZKSENMAGNETICMA73"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MA730', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-16-1EP_3x3mm_P0.5mm_EP1.8x1.8mm', 'kicadSymbolDatasheet': 'https://www.monolithicpower.com/pub/media/document/m/a/ma730_r1.01.pdf', 'kicadSymbolki_keywords': 'sensor magnetic hall position rotation spi', 'kicadSymbolki_description': 'Magnetic rotary angle sensor, 14-bit, SPI interface, ABZ, PWM, QFN-16', 'kicadSymbolki_fp_filters': 'QFN*3x3mm*P0.5mm*EP1.8x1.8mm*'}])
    newPart['name'].append('Sensor_Magnetic : MA730')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

