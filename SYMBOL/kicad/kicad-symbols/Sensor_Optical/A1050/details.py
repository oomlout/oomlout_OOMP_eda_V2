
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "A1050"
    hexID = "SZKSENOPTICALA15"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'R', 'kicadSymbolValue': 'A1050', 'kicadSymbolFootprint': 'OptoDevice:R_LDR_D6.4mm_P3.4mm_Vertical', 'kicadSymbolDatasheet': 'http://cdn-reichelt.de/documents/datenblatt/A500/A106012.pdf', 'kicadSymbolki_keywords': 'light dependent photo resistor LDR', 'kicadSymbolki_description': 'light dependent resistor', 'kicadSymbolki_fp_filters': 'R*LDR*D6.4*P3.4*'}])
    newPart['name'].append('Sensor_Optical : A1050')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

