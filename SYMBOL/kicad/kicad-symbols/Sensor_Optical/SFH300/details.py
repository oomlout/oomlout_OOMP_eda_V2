
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "SFH300"
    hexID = "SZKSENOPTICALSFH3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BPW40', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'SFH300', 'kicadSymbolFootprint': 'LED_THT:LED_D5.0mm_Clear', 'kicadSymbolDatasheet': 'http://www.osram-os.com/Graphics/XPic2/00101785_0.pdf', 'kicadSymbolki_keywords': 'NPN phototransistor', 'kicadSymbolki_description': 'silicon NPN phototransistor', 'kicadSymbolki_fp_filters': 'LED*D5.0mm*Clear*'}])
    newPart['name'].append('Sensor_Optical : SFH300')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

