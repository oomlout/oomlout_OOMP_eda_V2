
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "DNA40U2200GU"
    hexID = "SZKDIODEBRIDGEDNA4U22GU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'GUO40-08NO1', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'DNA40U2200GU', 'kicadSymbolFootprint': 'Diode_THT:Diode_Bridge_IXYS_GUFP', 'kicadSymbolDatasheet': 'https://ixapps.ixys.com/Datasheet/DNA40U2200GU.pdf', 'kicadSymbolki_keywords': 'Three-Phase Bridge Rectifier', 'kicadSymbolki_description': '690V Vrms, 40A If, GUFP(X025B)', 'kicadSymbolki_fp_filters': 'Diode*Bridge*IXYS*GUFP*'}])
    newPart['name'].append('DNA40U2200GU')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

