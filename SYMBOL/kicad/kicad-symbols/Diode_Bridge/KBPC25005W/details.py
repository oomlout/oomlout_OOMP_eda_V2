
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "KBPC25005W"
    hexID = "SZKDIODEBRIDGEKBPC255W"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'B40C1500G', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'KBPC25005W', 'kicadSymbolFootprint': 'Diode_THT:Diode_Bridge_GeneSiC_KBPC_W', 'kicadSymbolDatasheet': 'https://www.diodemodule.com/bridge-rectifier/kbpc/kbpc25005t.pdf', 'kicadSymbolki_keywords': 'diode full', 'kicadSymbolki_description': 'Single-Phase Bridge Rectifier, 35V Vrms, 25A If, KBPC-W(WS)', 'kicadSymbolki_fp_filters': 'Diode*Bridge*KBPC?W*'}])
    newPart['name'].append('Diode_Bridge : KBPC25005W')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

