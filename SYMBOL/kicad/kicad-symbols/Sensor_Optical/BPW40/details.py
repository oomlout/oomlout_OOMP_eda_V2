
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "BPW40"
    hexID = "SZKSENOPTICALBPW4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BPW40', 'kicadSymbolFootprint': 'LED_THT:LED_D5.0mm_Clear', 'kicadSymbolDatasheet': 'https://www.rcscomponents.kiev.ua/datasheets/bpw40.pdf', 'kicadSymbolki_keywords': 'npn phototransistor', 'kicadSymbolki_description': 'Phototransistor NPN', 'kicadSymbolki_fp_filters': 'LED*D5.0mm*Clear*'}])
    newPart['name'].append('BPW40')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

