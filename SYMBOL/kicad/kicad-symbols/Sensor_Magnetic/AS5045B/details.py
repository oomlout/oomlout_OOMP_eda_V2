
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Magnetic"
    oIndex = "AS5045B"
    hexID = "SZKSENMAGNETICAS545B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AS5045B', 'kicadSymbolFootprint': 'Package_SO:SSOP-16_5.3x6.2mm_P0.65mm', 'kicadSymbolDatasheet': 'https://ams.com/documents/20143/36005/AS5045B_DS000397_2-00.pdf', 'kicadSymbolki_keywords': 'Magnetic Hall Encoder', 'kicadSymbolki_description': 'Magnetic Position Sensor, 12-bit, PWM Output, ABI Output, SPI Interface, SSOP-16', 'kicadSymbolki_fp_filters': 'SSOP*5.3x6.2mm*P0.65mm*'}])
    newPart['name'].append('Sensor_Magnetic : AS5045B')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

