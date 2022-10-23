
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM5175PWP"
    hexID = "SZKREGULATORSWITCHINGLM5175PWP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM5175PWP', 'kicadSymbolFootprint': 'Package_SO:HTSSOP-28-1EP_4.4x9.7mm_P0.65mm_EP3.4x9.5mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm5175.pdf', 'kicadSymbolki_keywords': 'Buck Boost step-up step-down', 'kicadSymbolki_description': '42-V wide Vin synchronous 4-switch Buck-Boost controller, HTSSOP-28 package', 'kicadSymbolki_fp_filters': 'HTSSOP*4.4x9.7mm*P0.65*ThermalVias*'}])
    newPart['name'].append('LM5175PWP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

