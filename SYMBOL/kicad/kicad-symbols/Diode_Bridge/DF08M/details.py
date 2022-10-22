
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "DF08M"
    hexID = "SZKDIODEBRIDGEDF8M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'B40C800DM', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'DF08M', 'kicadSymbolFootprint': 'Diode_THT:Diode_Bridge_DIP-4_W7.62mm_P5.08mm', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/88571/dfm.pdf', 'kicadSymbolki_keywords': 'rectifier acdc', 'kicadSymbolki_description': 'Miniature Glass Passivated Single-Phase Bridge Rectifiers, 560V Vrms, 1.0A If, DIP-4', 'kicadSymbolki_fp_filters': 'Diode*Bridge*DIP*W7.62mm*P5.08mm*'}])
    newPart['name'].append('DF08M')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

