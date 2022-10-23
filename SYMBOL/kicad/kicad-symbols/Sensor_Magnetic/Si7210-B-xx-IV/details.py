
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Magnetic"
    oIndex = "Si7210-B-xx-IV"
    hexID = "SZKSENMAGNETICSI721BXXIV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'Si7210-B-xx-IV', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/si7210-datasheet.pdf', 'kicadSymbolki_keywords': 'I2C hall effect magnetic postition temperature sensor', 'kicadSymbolki_description': 'I2C Hall Effect Magnetic Position and Temperature Sensor, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT-23-5*'}])
    newPart['name'].append('Si7210-B-xx-IV')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

