
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Magnetic"
    oIndex = "MMC5883MA"
    hexID = "SZKSENMAGNETICC5883MA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MMC5883MA', 'kicadSymbolFootprint': 'Package_LGA:LGA-16_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.memsic.com/userfiles/files/DataSheets/Magnetic-Sensors-Datasheets/MMC5883MA-RevC.pdf', 'kicadSymbolki_keywords': 'I2C magnetic 3-axis sensor', 'kicadSymbolki_description': '3-axis Magnetic Sensor, I2C Interface, LGA-16', 'kicadSymbolki_fp_filters': '*LGA*3x3mm*P0.5mm*'}])
    newPart['name'].append('Sensor_Magnetic : MMC5883MA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

