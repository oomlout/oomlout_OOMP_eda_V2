
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Humidity"
    oIndex = "ENS210"
    hexID = "SZKSENHUMIDITYENS21"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ENS210', 'kicadSymbolFootprint': 'Package_DFN_QFN:AMS_QFN-4-1EP_2x2mm_P0.95mm_EP0.7x1.6mm', 'kicadSymbolDatasheet': 'http://ams.com/eng/Products/Environmental-Sensors/Relative-Humidity-and-Temperature-Sensors/ENS210', 'kicadSymbolki_keywords': 'relative humidity temperature i2c pre-calibrated', 'kicadSymbolki_description': 'Relative Humidity and Temperature Sensor with I2C Interface', 'kicadSymbolki_fp_filters': 'AMS?QFN*EP*2x2mm*P0.95mm*'}])
    newPart['name'].append('ENS210')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

