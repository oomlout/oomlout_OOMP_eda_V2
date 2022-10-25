
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "TPS22810DRV"
    hexID = "SZKPOWERMANAGEMENTTPS2281DRV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS22810DRV', 'kicadSymbolFootprint': 'Package_SON:WSON-6-1EP_2x2mm_P0.65mm_EP1x1.6mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps22810.pdf', 'kicadSymbolki_keywords': 'load switch thermal protection', 'kicadSymbolki_description': '2.7-18V, 79mohms On-Resistance Load Switch With Thermal Protection, WSON-6', 'kicadSymbolki_fp_filters': 'WSON*1EP*2x2mm*P0.65mm*'}])
    newPart['name'].append('Power_Management : TPS22810DRV')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

