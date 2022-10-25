
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "FRT5"
    hexID = "SZKRELAYFRT5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'FRT5', 'kicadSymbolFootprint': 'Relay_THT:Relay_DPDT_FRT5', 'kicadSymbolDatasheet': 'https://www.elpro.org/de/index.php?controller=attachment&id_attachment=8663', 'kicadSymbolki_keywords': 'relay monostable', 'kicadSymbolki_description': 'FORWARD INDUSTRIAL, Miniature Dual Pole Relay, DIP-like package', 'kicadSymbolki_fp_filters': 'Relay*DPDT*FRT5*'}])
    newPart['name'].append('Relay : FRT5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

