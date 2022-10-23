
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "DS1621V"
    hexID = "SZKSENTEMPERATUREDS1621V"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DS1621V', 'kicadSymbolFootprint': 'Package_SO:SO-8_5.3x6.2mm_P1.27mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/DS1621.pdf', 'kicadSymbolki_keywords': 'OneWire 1-Wire 1Wire Maxim Dallas', 'kicadSymbolki_description': '1-Wire Digital Thermometer and Thermostat, SO-8', 'kicadSymbolki_fp_filters': 'SO*5.3x6.2mm*P1.27mm*'}])
    newPart['name'].append('DS1621V')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

