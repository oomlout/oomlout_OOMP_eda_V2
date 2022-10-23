
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Motion"
    oIndex = "KXTJ3-1057"
    hexID = "SZKSENMOTIONKXTJ3157"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'KXTJ3-1057', 'kicadSymbolFootprint': 'Package_LGA:Kionix_LGA-12_2x2mm_P0.5mm_LayoutBorder2x4y', 'kicadSymbolDatasheet': 'http://kionixfs.kionix.com/en/datasheet/KXTJ3-1057-Specifications-Rev-5.0.pdf', 'kicadSymbolki_keywords': 'accelerometer, tri-axis, i2c', 'kicadSymbolki_description': '±2g / 4g / 8g / 16g Tri-Axis Digital Accelerometer, I2C, 1.71-3.6V, LGA-12', 'kicadSymbolki_fp_filters': 'Kionix*LGA-12*2x2mm*P0.5mm*'}])
    newPart['name'].append('KXTJ3-1057')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

