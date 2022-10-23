
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "DS1822"
    hexID = "SZKSENTEMPERATUREDS1822"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX31820', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DS1822', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'http://datasheets.maximintegrated.com/en/ds/DS1822.pdf', 'kicadSymbolki_keywords': 'OneWire 1Wire Dallas Maxim', 'kicadSymbolki_description': 'Econo 1-Wire Digital Thermometer TO-92', 'kicadSymbolki_fp_filters': 'TO*92*'}])
    newPart['name'].append('DS1822')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

