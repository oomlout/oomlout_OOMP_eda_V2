
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Proximity"
    oIndex = "LDC1612"
    hexID = "SZKSENPROXIMITYLDC1612"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LDC1312', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LDC1612', 'kicadSymbolFootprint': 'Package_SON:WSON-12-1EP_4x4mm_P0.5mm_EP2.6x3mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ldc1612.pdf', 'kicadSymbolki_keywords': 'inductance sensor', 'kicadSymbolki_description': 'Inductance to digital converter, 2-channel 28-bit, WSON-12', 'kicadSymbolki_fp_filters': 'WSON*1EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('LDC1612')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

