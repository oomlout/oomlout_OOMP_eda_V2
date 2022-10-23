
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Voltage"
    oIndex = "LV25-P"
    hexID = "SZKSENVOLTAGELV25P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LV25-P', 'kicadSymbolFootprint': 'Sensor_Voltage:LEM_LV25-P', 'kicadSymbolDatasheet': 'https://www.lem.com/sites/default/files/products_datasheets/lv_25-p.pdf', 'kicadSymbolki_keywords': 'Voltage transducer', 'kicadSymbolki_description': 'LEM Voltage transducer LV 25-P', 'kicadSymbolki_fp_filters': 'LEM?LV25?P*'}])
    newPart['name'].append('LV25-P')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

