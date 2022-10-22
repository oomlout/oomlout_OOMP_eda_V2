
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "GUO40-08NO1"
    hexID = "SZKDIODEBRIDGEGUO48NO1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'GUO40-08NO1', 'kicadSymbolFootprint': 'Diode_THT:Diode_Bridge_IXYS_GUFP', 'kicadSymbolDatasheet': 'https://ixapps.ixys.com/DataSheet/GUO40-08NO1.pdf', 'kicadSymbolki_keywords': 'Three-Phase Bridge Rectifier', 'kicadSymbolki_description': '250V Vrms, 40A If, GUFP(X025B)', 'kicadSymbolki_fp_filters': 'Diode*Bridge*IXYS*GUFP*'}])
    newPart['name'].append('GUO40-08NO1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

