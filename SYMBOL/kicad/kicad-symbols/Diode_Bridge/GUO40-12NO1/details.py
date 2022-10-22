
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "GUO40-12NO1"
    hexID = "SZKDIODEBRIDGEGUO412NO1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'GUO40-08NO1', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'GUO40-12NO1', 'kicadSymbolFootprint': 'Diode_THT:Diode_Bridge_IXYS_GUFP', 'kicadSymbolDatasheet': 'https://ixapps.ixys.com/DataSheet/GUO40-12NO1.pdf', 'kicadSymbolki_keywords': 'Three-Phase Bridge Rectifier', 'kicadSymbolki_description': '400V Vrms, 40A If, GUFP(X025B)', 'kicadSymbolki_fp_filters': 'Diode*Bridge*IXYS*GUFP*'}])
    newPart['name'].append('GUO40-12NO1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

