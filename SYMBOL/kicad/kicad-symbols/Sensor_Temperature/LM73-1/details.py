
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "LM73-1"
    hexID = "SZKSENTEMPERATURELM731"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM73', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM73-1', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-6', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm73.pdf', 'kicadSymbolki_keywords': 'digital temperature sensor', 'kicadSymbolki_description': '11 to 14 Bit digital temperature sensor with 2 wire interface, SOT23-6', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('LM73-1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

