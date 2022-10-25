
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Gas"
    oIndex = "LuminOX_LOX-O2"
    hexID = "SZKSENGASLUMINOXLOXO2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LuminOX_LOX-O2', 'kicadSymbolFootprint': 'Sensor:LuminOX_LOX-O2', 'kicadSymbolDatasheet': 'https://sstsensing.com/wp-content/uploads/2021/08/DS0030rev15_LuminOx.pdf', 'kicadSymbolki_keywords': 'O2 sensor', 'kicadSymbolki_description': 'SST LuminOX Luminescence-based O2 sensor', 'kicadSymbolki_fp_filters': 'LuminOX?LOX?O2*'}])
    newPart['name'].append('Sensor_Gas : LuminOX_LOX-O2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

