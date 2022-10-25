
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "AS72651"
    hexID = "SZKSENOPTICALAS72651"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AS72651', 'kicadSymbolFootprint': 'Package_LGA:AMS_LGA-20_4.7x4.5mm_P0.65mm', 'kicadSymbolDatasheet': 'https://ams.com/documents/20143/36005/AS7265x_DS000612_1-00.pdf/08051c8a-a7f6-6231-7993-2d3fe0bf38b8', 'kicadSymbolki_keywords': 'Smart Spectral Sensor', 'kicadSymbolki_description': 'Smart 18-Channel VIS+NIR Spectral_ID Sensor with Electronic Shutter, LGA-20', 'kicadSymbolki_fp_filters': 'AMS?LGA*4.7x4.5mm*P0.65mm*'}])
    newPart['name'].append('Sensor_Optical : AS72651')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

