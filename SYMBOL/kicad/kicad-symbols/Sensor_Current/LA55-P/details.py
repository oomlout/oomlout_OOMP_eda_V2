
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "LA55-P"
    hexID = "SZKSENCURRENTLA55P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LA25-P', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LA55-P', 'kicadSymbolFootprint': 'Sensor_Current:LEM_LA25-P', 'kicadSymbolDatasheet': 'https://www.lem.com/sites/default/files/products_datasheets/la_55-p_e.pdf', 'kicadSymbolki_keywords': 'current transducer', 'kicadSymbolki_description': 'Current Transducer, 50A, Bipolar, +/-15V', 'kicadSymbolki_fp_filters': 'LEM*LA25*P*'}])
    newPart['name'].append('LA55-P')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

