
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM5176RHF"
    hexID = "SZKREGULATORSWITCHINGLM5176RHF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM5175RHF', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM5176RHF', 'kicadSymbolFootprint': 'Package_DFN_QFN:VQFN-28-1EP_4x5mm_P0.5mm_EP2.55x3.55mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm5176.pdf', 'kicadSymbolki_keywords': 'Buck Boost step-up step-down', 'kicadSymbolki_description': '55-V wide Vin synchronous 4-switch Buck-Boost controller, QFN-28 package', 'kicadSymbolki_fp_filters': 'VQFN*4x5mm*P0.5*'}])
    newPart['name'].append('LM5176RHF')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

