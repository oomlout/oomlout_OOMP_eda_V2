
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "BP103B"
    hexID = "SZKSENOPTICALBP13B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BPW40', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BP103B', 'kicadSymbolFootprint': 'LED_THT:LED_D5.0mm_Clear', 'kicadSymbolDatasheet': 'http://www.b-kainka.de/Daten/Sensor/bp103bf.pdf', 'kicadSymbolki_keywords': 'NPN phototransistor', 'kicadSymbolki_description': 'NPN phototransistor', 'kicadSymbolki_fp_filters': 'LED*D5.0mm*Clear*'}])
    newPart['name'].append('BP103B')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

