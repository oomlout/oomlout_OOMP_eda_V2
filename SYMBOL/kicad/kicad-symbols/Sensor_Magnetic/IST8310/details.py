
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Magnetic"
    oIndex = "IST8310"
    hexID = "SZKSENMAGNETICIST831"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IST8310', 'kicadSymbolFootprint': 'Package_LGA:LGA-16_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.isentek.com/en/dlf.php?file=../ISENTEK/(201703-09)IST8310%20Datasheet%20v1.2_brief-105.09.20.pdf', 'kicadSymbolki_keywords': 'magnet field sensor compass', 'kicadSymbolki_description': '3D Magnetometer, I2C Interface, LGA-16', 'kicadSymbolki_fp_filters': 'LGA*3x3mm*P0.5mm*'}])
    newPart['name'].append('IST8310')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

