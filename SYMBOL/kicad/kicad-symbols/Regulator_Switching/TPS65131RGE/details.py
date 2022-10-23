
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS65131RGE"
    hexID = "SZKREGULATORSWITCHINGTPS65131RGE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS65130RGE', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS65131RGE', 'kicadSymbolFootprint': 'Package_DFN_QFN:VQFN-24-1EP_4x4mm_P0.5mm_EP2.45x2.45mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps65130.pdf', 'kicadSymbolki_keywords': 'split-rail switching dual positive negative', 'kicadSymbolki_description': 'Split-Rail Converter with Dual, Positive and Negative Outputs (750mA typ, Switch Current Limit 1950mA typ),), 2.7-5.5V, VQFN-24', 'kicadSymbolki_fp_filters': 'VQFN*1EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('TPS65131RGE')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

