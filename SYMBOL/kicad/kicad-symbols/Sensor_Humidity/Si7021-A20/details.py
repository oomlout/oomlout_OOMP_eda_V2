
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Humidity"
    oIndex = "Si7021-A20"
    hexID = "SZKSENHUMIDITYSI721A2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'Si7020-A20', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'Si7021-A20', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-6-1EP_3x3mm_P1mm_EP1.5x2.4mm', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/Si7021-A20.pdf', 'kicadSymbolki_keywords': 'I2C Humidity Temperature Sensor', 'kicadSymbolki_description': 'I2C Humidity and Temperature Sensor, DFN-6', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x3mm*P1mm*'}])
    newPart['name'].append('Si7021-A20')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

