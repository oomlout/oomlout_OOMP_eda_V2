
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "KBPC3510T"
    hexID = "SZKDIODEBRIDGEKBPC351T"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'B40C1500G', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'KBPC3510T', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.diodemodule.com/bridge-rectifier/kbpc/kbpc3510t.pdf', 'kicadSymbolki_keywords': 'diode full', 'kicadSymbolki_description': 'Single-Phase Bridge Rectifier, 700V Vrms, 35A If, KBPC-T(FP)', 'kicadSymbolki_fp_filters': 'Diode*Bridge*KBPC?T*'}])
    newPart['name'].append('Diode_Bridge : KBPC3510T')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

