
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "HX02-P"
    hexID = "SZKSENCURRENTHX2P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HX02-P', 'kicadSymbolFootprint': 'Sensor_Current:LEM_HX02-P', 'kicadSymbolDatasheet': 'https://www.lem.com/sites/default/files/products_datasheets/hx%202_6-p_e%20v5.pdf', 'kicadSymbolki_keywords': 'current transducer', 'kicadSymbolki_description': 'Current Transducer, 2A, Bipolar, +/-15V', 'kicadSymbolki_fp_filters': 'LEM*HX02*P*'}])
    newPart['name'].append('Sensor_Current : HX02-P')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

