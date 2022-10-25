
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "A9013"
    hexID = "SZKSENOPTICALA913"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'A9050', 'kicadSymbolReference': 'R', 'kicadSymbolValue': 'A9013', 'kicadSymbolFootprint': 'OptoDevice:R_LDR_5.0x4.1mm_P3mm_Vertical', 'kicadSymbolDatasheet': 'http://www.produktinfo.conrad.com/datenblaetter/125000-149999/145475-da-01-en-FOTOWIDERSTAND_A_9060_A_9013.pdf', 'kicadSymbolki_keywords': 'light dependent photo resistor LDR', 'kicadSymbolki_description': 'light dependent resistor', 'kicadSymbolki_fp_filters': 'R*LDR*5.0x4.1mm*P3mm*'}])
    newPart['name'].append('Sensor_Optical : A9013')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

