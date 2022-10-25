
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Magnetic"
    oIndex = "Si7210-B-xx-IM2"
    hexID = "SZKSENMAGNETICSI721BXXIM2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'Si7210-B-xx-IM2', 'kicadSymbolFootprint': 'Package_DFN_QFN:TDFN-8_1.4x1.6mm_P0.4mm', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/si7210-datasheet.pdf', 'kicadSymbolki_keywords': 'I2C hall effect magnetic postition temperature sensor', 'kicadSymbolki_description': 'I2C Hall Effect Magnetic Position and Temperature Sensor, TDFN-8', 'kicadSymbolki_fp_filters': 'TDFN-8*1.4x1.6mm*P0.4mm*'}])
    newPart['name'].append('Sensor_Magnetic : Si7210-B-xx-IM2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

