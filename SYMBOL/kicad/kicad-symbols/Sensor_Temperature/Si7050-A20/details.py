
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "Si7050-A20"
    hexID = "SZKSENTEMPERATURESI75A2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'Si7050-A20', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-6-1EP_3x3mm_P1mm_EP1.65x2.55mm', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/Si7050-1-3-4-5-A20.pdf', 'kicadSymbolki_keywords': 'I2C Temperature Sensor', 'kicadSymbolki_description': 'I2C Temperature Sensor, ±1.0ºC, DFN-6', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x3mm*P1mm*'}])
    newPart['name'].append('Si7050-A20')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

