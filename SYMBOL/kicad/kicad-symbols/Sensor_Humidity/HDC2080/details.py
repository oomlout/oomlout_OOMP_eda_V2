
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Humidity"
    oIndex = "HDC2080"
    hexID = "SZKSENHUMIDITYHDC28"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HDC2080', 'kicadSymbolFootprint': 'Package_SON:Texas_PWSON-N6', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/hdc2080.pdf', 'kicadSymbolki_keywords': 'Temperature Humidity Sensor', 'kicadSymbolki_description': 'Low Power Humidity and Temperature Sensor', 'kicadSymbolki_fp_filters': 'Package*SON:Texas*PWSON*N6*'}])
    newPart['name'].append('Sensor_Humidity : HDC2080')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

