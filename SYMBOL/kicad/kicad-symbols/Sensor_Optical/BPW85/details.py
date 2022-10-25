
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "BPW85"
    hexID = "SZKSENOPTICALBPW85"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SFH309', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BPW85', 'kicadSymbolFootprint': 'LED_THT:LED_D3.0mm_Clear', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/81531/bpw85a.pdf', 'kicadSymbolki_keywords': 'npn phototransistor', 'kicadSymbolki_description': 'Silicon NPN Phototransistor, Ica = 0.8-8mA, T-1', 'kicadSymbolki_fp_filters': 'LED*3.0mm*Clear*'}])
    newPart['name'].append('Sensor_Optical : BPW85')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

