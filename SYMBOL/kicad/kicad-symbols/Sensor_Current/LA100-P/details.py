
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "LA100-P"
    hexID = "SZKSENCURRENTLA1P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LA25-P', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LA100-P', 'kicadSymbolFootprint': 'Sensor_Current:LEM_LA25-P', 'kicadSymbolDatasheet': 'https://www.lem.com/sites/default/files/products_datasheets/la_100-p_e_.pdf', 'kicadSymbolki_keywords': 'current transducer', 'kicadSymbolki_description': 'Current Transducer, 100A, Bipolar, +/-15V', 'kicadSymbolki_fp_filters': 'LEM*LA25*P*'}])
    newPart['name'].append('LA100-P')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

