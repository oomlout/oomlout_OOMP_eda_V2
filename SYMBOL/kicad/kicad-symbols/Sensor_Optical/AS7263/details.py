
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "AS7263"
    hexID = "SZKSENOPTICALAS7263"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AS7261', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AS7263', 'kicadSymbolFootprint': 'Package_LGA:AMS_LGA-20_4.7x4.5mm_P0.65mm', 'kicadSymbolDatasheet': 'http://ams.com/eng/content/download/976611/2309519/498778', 'kicadSymbolki_keywords': '6-Channel NIR Spectral_ID Device Electronic Shutter Smart Interface i2c uart', 'kicadSymbolki_description': 'Spectral Sensing Engine, 6-Channel NIR Spectral_ID', 'kicadSymbolki_fp_filters': 'AMS?LGA*4.7x4.5mm*P0.65mm*'}])
    newPart['name'].append('Sensor_Optical : AS7263')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

