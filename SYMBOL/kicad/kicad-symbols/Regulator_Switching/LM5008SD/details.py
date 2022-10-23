
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM5008SD"
    hexID = "SZKREGULATORSWITCHINGLM58SD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM5007SD', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM5008SD', 'kicadSymbolFootprint': 'Package_SON:WSON-8-1EP_4x4mm_P0.8mm_EP2.6x3mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm5008.pdf', 'kicadSymbolki_keywords': 'Step-Down Switching Regulator', 'kicadSymbolki_description': '500mA, High Voltage (100V) Step-Down Switching Regulator, Adjustable Output Voltage, WSON-8', 'kicadSymbolki_fp_filters': 'WSON*1EP*4x4mm*P0.8mm*'}])
    newPart['name'].append('LM5008SD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

