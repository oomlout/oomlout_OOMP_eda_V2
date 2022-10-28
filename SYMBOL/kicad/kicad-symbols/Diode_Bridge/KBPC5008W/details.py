
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "KBPC5008W"
    hexID = "SZKDIODEBRIDGEKBPC58W"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'B40C1500G', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'KBPC5008W', 'kicadSymbolFootprint': 'Diode_THT:Diode_Bridge_GeneSiC_KBPC_W', 'kicadSymbolDatasheet': 'https://www.diodemodule.com/bridge-rectifier/kbpc/kbpc5008t.pdf', 'kicadSymbolki_keywords': 'diode full', 'kicadSymbolki_description': 'Single-Phase Bridge Rectifier, 560V Vrms, 50A If, KBPC-W(WS)', 'kicadSymbolki_fp_filters': 'Diode*Bridge*KBPC?W*'}])
    newPart['name'].append('Diode_Bridge : KBPC5008W')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

