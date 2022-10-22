
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "B250C800DM"
    hexID = "SZKDIODEBRIDGEB25C8DM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'B40C800DM', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'B250C800DM', 'kicadSymbolFootprint': 'Diode_THT:Diode_Bridge_DIP-4_W7.62mm_P5.08mm', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/88533/800dm.pdf', 'kicadSymbolki_keywords': 'rectifier acdc', 'kicadSymbolki_description': 'Glass Passivated Single-Phase Bridge Rectifier, 250V Vrms, 0.8A If, DIP-4', 'kicadSymbolki_fp_filters': 'Diode*Bridge*DIP*W7.62mm*P5.08mm*'}])
    newPart['name'].append('B250C800DM')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

