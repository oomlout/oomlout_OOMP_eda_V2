
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "BP103"
    hexID = "SZKSENOPTICALBP13"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BP103', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-18-3_Lens', 'kicadSymbolDatasheet': 'http://www.osram-os.com/Graphics/XPic3/00101777_0.pdf/BP', 'kicadSymbolki_keywords': 'npn phototransistor', 'kicadSymbolki_description': 'NPN Phototransistor', 'kicadSymbolki_fp_filters': 'TO?18*Lens*'}])
    newPart['name'].append('Sensor_Optical : BP103')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

