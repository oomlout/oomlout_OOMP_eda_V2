
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "FRT5_separated"
    hexID = "SZKRELAYFRT5SEPARATED"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'FRT5_separated', 'kicadSymbolFootprint': 'Relay_THT:Relay_DPDT_FRT5', 'kicadSymbolDatasheet': 'https://www.elpro.org/de/index.php?controller=attachment&id_attachment=8663', 'kicadSymbolki_keywords': 'relay monostable', 'kicadSymbolki_description': 'FORWARD INDUSTRIAL, Miniature Dual Pole Relay, DIP-like package, separate subsymbols', 'kicadSymbolki_fp_filters': 'Relay*DPDT*FRT5*'}])
    newPart['name'].append('FRT5_separated')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

