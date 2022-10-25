
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Proximity"
    oIndex = "LDC1312"
    hexID = "SZKSENPROXIMITYLDC1312"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LDC1312', 'kicadSymbolFootprint': 'Package_SON:WSON-12-1EP_4x4mm_P0.5mm_EP2.6x3mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ldc1312.pdf', 'kicadSymbolki_keywords': 'inductance sensor', 'kicadSymbolki_description': 'Inductance to digital converter, 2-channel 12-bit, WSON-12', 'kicadSymbolki_fp_filters': 'WSON*1EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('Sensor_Proximity : LDC1312')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

