
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM2595T-ADJ"
    hexID = "SZKREGULATORSWITCHINGLM2595TADJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM2595T-12', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2595T-ADJ', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-5_P3.4x3.7mm_StaggerOdd_Lead3.8mm_Vertical', 'kicadSymbolDatasheet': 'http://www.ti.com.cn/cn/lit/ds/symlink/lm2595.pdf', 'kicadSymbolki_keywords': 'Step-Down Voltage Regulator 1A Adjustable', 'kicadSymbolki_description': 'Adjustable Output 1A Step-Down Voltage Regulator, TO-220-5', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('LM2595T-ADJ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

