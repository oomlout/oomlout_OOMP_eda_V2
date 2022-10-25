
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "TEPT4400"
    hexID = "SZKSENOPTICALTEPT44"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SFH309', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'TEPT4400', 'kicadSymbolFootprint': 'LED_THT:LED_D3.0mm_Clear', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/81341/tept4400.pdf', 'kicadSymbolki_keywords': 'npn phototransistor ambient light sensor', 'kicadSymbolki_description': 'Ambient Light Sensor, NPN Epitaxial Planar Phototransistor, T-1', 'kicadSymbolki_fp_filters': 'LED*3.0mm*Clear*'}])
    newPart['name'].append('Sensor_Optical : TEPT4400')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

