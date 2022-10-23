
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Magnetic"
    oIndex = "IST8308"
    hexID = "SZKSENMAGNETICIST838"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IST8310', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IST8308', 'kicadSymbolFootprint': 'Package_LGA:LGA-16_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.isentek.com/en/dlf.php?file=../ISENTEK/(201703-20)IST8308%20Datasheet%20v1.0_brief.pdf', 'kicadSymbolki_keywords': 'magnet field sensor compass', 'kicadSymbolki_description': '3D Magnetometer, High Sensitivity, I2C Interface, LGA-16', 'kicadSymbolki_fp_filters': 'LGA*3x3mm*P0.5mm*'}])
    newPart['name'].append('IST8308')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

