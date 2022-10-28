
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "KBPC5004T"
    hexID = "SZKDIODEBRIDGEKBPC54T"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'B40C1500G', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'KBPC5004T', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.diodemodule.com/bridge-rectifier/kbpc/kbpc5004t.pdf', 'kicadSymbolki_keywords': 'diode full', 'kicadSymbolki_description': 'Single-Phase Bridge Rectifier, 280V Vrms, 50A If, KBPC-T(FP)', 'kicadSymbolki_fp_filters': 'Diode*Bridge*KBPC?T*'}])
    newPart['name'].append('Diode_Bridge : KBPC5004T')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

