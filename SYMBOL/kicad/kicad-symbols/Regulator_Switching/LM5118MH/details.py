
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM5118MH"
    hexID = "SZKREGULATORSWITCHINGLM5118MH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM5118MH', 'kicadSymbolFootprint': 'Package_SO:Texas_PWP0020A', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/lm5118.pdf', 'kicadSymbolki_keywords': 'Buck Boost step-up step-down', 'kicadSymbolki_description': 'Wide Voltage Range Buck-Boost Controller, HTSSOP-20', 'kicadSymbolki_fp_filters': 'Texas*PWP0020A*'}])
    newPart['name'].append('LM5118MH')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

