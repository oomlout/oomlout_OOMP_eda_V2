
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM5017SD"
    hexID = "SZKREGULATORSWITCHINGLM517SD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM5017SD', 'kicadSymbolFootprint': 'Package_SON:WSON-8-1EP_4x4mm_P0.8mm_EP1.98x3mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm5017.pdf', 'kicadSymbolki_keywords': 'Step-Down Switching Regulator High Voltage', 'kicadSymbolki_description': '600mA, 100V Step-Down Switching Regulator, WSON-8', 'kicadSymbolki_fp_filters': 'WSON*1EP*4x4mm*P0.8mm*'}])
    newPart['name'].append('LM5017SD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

