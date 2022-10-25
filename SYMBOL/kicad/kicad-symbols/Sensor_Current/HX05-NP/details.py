
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "HX05-NP"
    hexID = "SZKSENCURRENTHX5NP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HX05-NP', 'kicadSymbolFootprint': 'Sensor_Current:LEM_HX05-NP', 'kicadSymbolDatasheet': 'https://www.lem.com/sites/default/files/products_datasheets/hx%205_15-np_e%20v10.pdf', 'kicadSymbolki_keywords': 'current transducer', 'kicadSymbolki_description': 'Current Transducer, 5A, Bipolar, +/-15V', 'kicadSymbolki_fp_filters': 'LEM*HX05*NP*'}])
    newPart['name'].append('Sensor_Current : HX05-NP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

