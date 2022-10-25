
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "BPW42"
    hexID = "SZKSENOPTICALBPW42"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SFH309', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BPW42', 'kicadSymbolFootprint': 'LED_THT:LED_D3.0mm_Clear', 'kicadSymbolDatasheet': 'http://www.ges.cz/sheets/b/bpw42.pdf', 'kicadSymbolki_keywords': 'NPN phototransistor opto', 'kicadSymbolki_description': 'NPN phototransistor', 'kicadSymbolki_fp_filters': 'LED*3.0mm*Clear*'}])
    newPart['name'].append('Sensor_Optical : BPW42')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

