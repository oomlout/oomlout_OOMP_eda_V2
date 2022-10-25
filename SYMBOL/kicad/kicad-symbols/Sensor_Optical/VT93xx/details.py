
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "VT93xx"
    hexID = "SZKSENOPTICALVT93XX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'R', 'kicadSymbolValue': 'VT93xx', 'kicadSymbolFootprint': 'OptoDevice:R_LDR_4.9x4.2mm_P2.54mm_Vertical', 'kicadSymbolDatasheet': 'http://www.produktinfo.conrad.com/datenblaetter/125000-149999/140375-da-01-en-FOTOWIDERSTAND__VT_93_N2__THT_.pdf', 'kicadSymbolki_keywords': 'light dependent photo resistor LDR', 'kicadSymbolki_description': 'light dependent resistor', 'kicadSymbolki_fp_filters': 'R*LDR*4.9x4.2mm*P2.54mm*'}])
    newPart['name'].append('Sensor_Optical : VT93xx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

