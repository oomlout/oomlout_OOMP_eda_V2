
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "HX10-NP"
    hexID = "SZKSENCURRENTHX1NP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HX10-NP', 'kicadSymbolFootprint': 'Sensor_Current:LEM_HX10-NP', 'kicadSymbolDatasheet': 'https://www.lem.com/sites/default/files/products_datasheets/hx%205_15-np_e%20v10.pdf', 'kicadSymbolki_keywords': 'current transducer', 'kicadSymbolki_description': 'Current Transducer, 10A, Bipolar, +/-15V', 'kicadSymbolki_fp_filters': 'LEM*HX10*NP*'}])
    newPart['name'].append('HX10-NP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

