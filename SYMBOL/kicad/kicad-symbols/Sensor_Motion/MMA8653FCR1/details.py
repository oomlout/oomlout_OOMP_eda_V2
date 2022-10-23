
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Motion"
    oIndex = "MMA8653FCR1"
    hexID = "SZKSENMOTIONA8653FCR1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MMA8653FCR1', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-10_2x2mm_P0.4mm', 'kicadSymbolDatasheet': 'http://cache.freescale.com/files/sensors/doc/data_sheet/MMA8653FC.pdf', 'kicadSymbolki_keywords': 'Accelerometer I2C', 'kicadSymbolki_description': '3-Axis 10-bit Digital Accelerometer with I2C interface', 'kicadSymbolki_fp_filters': 'DFN*2x2mm*P0.4mm*'}])
    newPart['name'].append('MMA8653FCR1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

