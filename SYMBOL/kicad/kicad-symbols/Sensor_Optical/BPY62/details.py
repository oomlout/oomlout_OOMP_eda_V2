
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "BPY62"
    hexID = "SZKSENOPTICALBPY62"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BP103', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BPY62', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-18-3_Lens', 'kicadSymbolDatasheet': 'http://www.osram-os.com/Graphics/XPic9/00208595_0.pdf', 'kicadSymbolki_keywords': 'NPN Phototransistor opto', 'kicadSymbolki_description': 'NPN Phototransistor', 'kicadSymbolki_fp_filters': 'TO?18*Lens*'}])
    newPart['name'].append('Sensor_Optical : BPY62')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

