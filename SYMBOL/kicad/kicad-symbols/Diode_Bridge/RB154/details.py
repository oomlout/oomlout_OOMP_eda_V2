
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "RB154"
    hexID = "SZKDIODEBRIDGERB154"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'B40R', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'RB154', 'kicadSymbolFootprint': 'Diode_THT:Diode_Bridge_Round_D9.0mm', 'kicadSymbolDatasheet': 'https://www.rectron.com/public/product_datasheets/rb151-rb157.pdf', 'kicadSymbolki_keywords': 'rectifier acdc', 'kicadSymbolki_description': 'Single-Phase Bridge Rectifier, 280V Vrms, 1.5A If, WOG-like package', 'kicadSymbolki_fp_filters': 'D*Bridge*Round*D9.0mm*'}])
    newPart['name'].append('RB154')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

