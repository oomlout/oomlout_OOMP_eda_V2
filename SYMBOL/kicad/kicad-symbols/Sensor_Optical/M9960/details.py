
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "M9960"
    hexID = "SZKSENOPTICALM996"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'R', 'kicadSymbolValue': 'M9960', 'kicadSymbolFootprint': 'OptoDevice:R_LDR_5.2x5.2mm_P3.5mm_Horizontal', 'kicadSymbolDatasheet': 'http://cdn-reichelt.de/documents/datenblatt/A500/M996011a_b.pdf', 'kicadSymbolki_keywords': 'light dependent photo resistor LDR', 'kicadSymbolki_description': 'light dependent resistor', 'kicadSymbolki_fp_filters': 'R*LDR*5.2x5.2mm*P3.5mm*'}])
    newPart['name'].append('Sensor_Optical : M9960')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

