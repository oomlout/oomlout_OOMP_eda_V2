
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "AS7261"
    hexID = "SZKSENOPTICALAS7261"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AS7261', 'kicadSymbolFootprint': 'Package_LGA:AMS_LGA-20_4.7x4.5mm_P0.65mm', 'kicadSymbolDatasheet': 'http://ams.com/eng/content/download/1008631/2361759/498838', 'kicadSymbolki_keywords': '6-Channel XYZ Spectral_ID Device Electronic Shutter Smart Interface i2c uart', 'kicadSymbolki_description': 'Spectral Sensing Engine, 6-Channel XYZ Spectral_ID', 'kicadSymbolki_fp_filters': 'AMS?LGA*4.7x4.5mm*P0.65mm*'}])
    newPart['name'].append('Sensor_Optical : AS7261')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

