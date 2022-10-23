
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "HX05-P-SP2"
    hexID = "SZKSENCURRENTHX5PSP2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HX05-P-SP2', 'kicadSymbolFootprint': 'Sensor_Current:LEM_HX05-P-SP2', 'kicadSymbolDatasheet': 'https://www.lem.com/sites/default/files/products_datasheets/hx%203_50-p_sp2_e%20v07.pdf', 'kicadSymbolki_keywords': 'current transducer', 'kicadSymbolki_description': 'Current Transducer, 5A, Unipolar, +/-15V', 'kicadSymbolki_fp_filters': 'LEM*HX05*P*SP2*'}])
    newPart['name'].append('HX05-P-SP2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

