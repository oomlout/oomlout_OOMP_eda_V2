
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "HX06-P"
    hexID = "SZKSENCURRENTHX6P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HX06-P', 'kicadSymbolFootprint': 'Sensor_Current:LEM_HX06-P', 'kicadSymbolDatasheet': 'https://www.lem.com/sites/default/files/products_datasheets/hx%202_6-p_e%20v5.pdf', 'kicadSymbolki_keywords': 'current transducer', 'kicadSymbolki_description': 'Current Transducer, 6A, Bipolar, +/-15V', 'kicadSymbolki_fp_filters': 'LEM*HX06*P*'}])
    newPart['name'].append('Sensor_Current : HX06-P')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

