
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "HTFS600-P"
    hexID = "SZKSENCURRENTHTFS6P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'HTFS200-P', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HTFS600-P', 'kicadSymbolFootprint': 'Sensor_Current:LEM_HTFS', 'kicadSymbolDatasheet': 'https://www.lem.com/sites/default/files/products_datasheets/htfs_200_800-p.pdf', 'kicadSymbolki_keywords': 'current transducer', 'kicadSymbolki_description': 'Current Transducer, 600A, Unipolar, 5V', 'kicadSymbolki_fp_filters': 'LEM*HTFS*'}])
    newPart['name'].append('Sensor_Current : HTFS600-P')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

