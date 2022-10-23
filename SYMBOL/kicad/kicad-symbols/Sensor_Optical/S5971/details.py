
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "S5971"
    hexID = "SZKSENOPTICALS5971"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'S5971', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-18-3', 'kicadSymbolDatasheet': 'https://www.hamamatsu.com/resources/pdf/ssd/s5971_etc_kpin1025e.pdf', 'kicadSymbolki_keywords': 'opto photodiode', 'kicadSymbolki_description': 'Si PIN Photodiode, 0.1 GHz, TO-18-3', 'kicadSymbolki_fp_filters': 'TO?18*'}])
    newPart['name'].append('S5971')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

