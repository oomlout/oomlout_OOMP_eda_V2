
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "HO8-NSM"
    hexID = "SZKSENCURRENTHO8NSM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HO8-NSM', 'kicadSymbolFootprint': 'Sensor_Current:LEM_HO8-NSM', 'kicadSymbolDatasheet': 'https://www.lem.com/sites/default/files/products_datasheets/ho-nsm-0000_series.pdf', 'kicadSymbolki_keywords': 'current transducer', 'kicadSymbolki_description': 'Current Transducer, 8A, Unipolar, 5V', 'kicadSymbolki_fp_filters': 'LEM*HO8*NSM*'}])
    newPart['name'].append('Sensor_Current : HO8-NSM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

