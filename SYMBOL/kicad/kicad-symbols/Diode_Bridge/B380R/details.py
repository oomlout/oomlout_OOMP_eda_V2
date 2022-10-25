
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "B380R"
    hexID = "SZKDIODEBRIDGEB38R"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'B40R', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'B380R', 'kicadSymbolFootprint': 'Diode_THT:Diode_Bridge_Round_D9.0mm', 'kicadSymbolDatasheet': 'https://diotec.com/tl_files/diotec/files/pdf/datasheets/b40r.pdf', 'kicadSymbolki_keywords': 'rectifier acdc', 'kicadSymbolki_description': 'Single-Phase Bridge Rectifier, 380V Vrms, 1.6A If, WOG-like package', 'kicadSymbolki_fp_filters': 'D*Bridge*Round*D9.0mm*'}])
    newPart['name'].append('Diode_Bridge : B380R')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

