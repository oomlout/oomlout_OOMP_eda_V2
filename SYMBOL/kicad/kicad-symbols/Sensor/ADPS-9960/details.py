
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor"
    oIndex = "ADPS-9960"
    hexID = "SZKSENADPS996"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADPS-9960', 'kicadSymbolFootprint': 'Sensor:Avago_ADPS-9960', 'kicadSymbolDatasheet': 'https://docs.broadcom.com/doc/AV02-4191EN', 'kicadSymbolki_keywords': 'sensor gesture light rgb', 'kicadSymbolki_description': 'Digital Proximity, Ambient Light, RGB and Gesture Sensor', 'kicadSymbolki_fp_filters': 'Avago?ADPS?9960*'}])
    newPart['name'].append('Sensor : ADPS-9960')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

