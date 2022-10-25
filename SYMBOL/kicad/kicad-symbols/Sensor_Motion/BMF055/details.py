
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Motion"
    oIndex = "BMF055"
    hexID = "SZKSENMOTIONBMF55"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BMF055', 'kicadSymbolFootprint': 'Package_LGA:LGA-28_5.2x3.8mm_P0.5mm', 'kicadSymbolDatasheet': 'https://ae-bst.resource.bosch.com/media/_tech/media/datasheets/BST-BMF055-DS000.pdf', 'kicadSymbolki_keywords': '9-axis motion sensor IMU SAMD20 ARM Cortex-M0+', 'kicadSymbolki_description': 'Custom programmable 9-axis motion sensor', 'kicadSymbolki_fp_filters': 'LGA*5.2x3.8mm*P0.5mm*'}])
    newPart['name'].append('Sensor_Motion : BMF055')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

