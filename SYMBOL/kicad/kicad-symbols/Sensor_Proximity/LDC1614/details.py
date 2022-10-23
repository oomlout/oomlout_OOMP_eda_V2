
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Proximity"
    oIndex = "LDC1614"
    hexID = "SZKSENPROXIMITYLDC1614"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LDC1314', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LDC1614', 'kicadSymbolFootprint': 'Package_DFN_QFN:WQFN-16-1EP_4x4mm_P0.5mm_EP2.6x2.6mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ldc1612.pdf', 'kicadSymbolki_keywords': 'inductance sensor', 'kicadSymbolki_description': 'Inductance to digital converter, 4-channel 28-bit, WQFN-16', 'kicadSymbolki_fp_filters': 'WQFN*1EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('LDC1614')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

