
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "TVS1400DRV"
    hexID = "SZKPOWERPROTECTIONTVS14DRV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TVS0500DRV', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TVS1400DRV', 'kicadSymbolFootprint': 'Package_SON:WSON-6-1EP_2x2mm_P0.65mm_EP1x1.6mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tvs1400.pdf', 'kicadSymbolki_keywords': 'EMI, ESD, TVS protection transient', 'kicadSymbolki_description': 'Flat-Clamp Surge Protection Device. 14Vrwm, WSON-6', 'kicadSymbolki_fp_filters': 'WSON*1EP*2x2mm*P0.65mm*EP1x1.6mm*'}])
    newPart['name'].append('Power_Protection : TVS1400DRV')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

