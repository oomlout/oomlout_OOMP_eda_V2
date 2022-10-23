
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Motion"
    oIndex = "BNO055"
    hexID = "SZKSENMOTIONBNO55"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BNO055', 'kicadSymbolFootprint': 'Package_LGA:LGA-28_5.2x3.8mm_P0.5mm', 'kicadSymbolDatasheet': 'https://ae-bst.resource.bosch.com/media/_tech/media/datasheets/BST_BNO055_DS000_14.pdf', 'kicadSymbolki_keywords': 'IMU, Sensor Fusion, I2C, UART', 'kicadSymbolki_description': 'Intelligent 9-axis absolute orientation sensor, LGA-28', 'kicadSymbolki_fp_filters': 'LGA*5.2x3.8mm*P0.5mm*'}])
    newPart['name'].append('BNO055')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

