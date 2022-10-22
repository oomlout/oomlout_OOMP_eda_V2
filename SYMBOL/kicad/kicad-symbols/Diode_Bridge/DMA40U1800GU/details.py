
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "DMA40U1800GU"
    hexID = "SZKDIODEBRIDGEDMA4U18GU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'GUO40-08NO1', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'DMA40U1800GU', 'kicadSymbolFootprint': 'Diode_THT:Diode_Bridge_IXYS_GUFP', 'kicadSymbolDatasheet': 'https://ixapps.ixys.com/Datasheet/DMA40U1800GU.pdf', 'kicadSymbolki_keywords': 'Three-Phase Bridge Rectifier', 'kicadSymbolki_description': '575V Vrms, 40A If, GUFP(X025B)', 'kicadSymbolki_fp_filters': 'Diode*Bridge*IXYS*GUFP*'}])
    newPart['name'].append('DMA40U1800GU')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

