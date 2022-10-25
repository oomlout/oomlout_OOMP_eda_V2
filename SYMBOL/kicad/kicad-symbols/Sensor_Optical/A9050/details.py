
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "A9050"
    hexID = "SZKSENOPTICALA95"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'R', 'kicadSymbolValue': 'A9050', 'kicadSymbolFootprint': 'OptoDevice:R_LDR_5.0x4.1mm_P3mm_Vertical', 'kicadSymbolDatasheet': 'http://cdn-reichelt.de/documents/datenblatt/A500/A90xxxx%23PE.pdf', 'kicadSymbolki_keywords': 'light dependent photo resistor LDR', 'kicadSymbolki_description': 'light dependent resistor', 'kicadSymbolki_fp_filters': 'R*LDR*5.0x4.1mm*P3mm*'}])
    newPart['name'].append('Sensor_Optical : A9050')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

