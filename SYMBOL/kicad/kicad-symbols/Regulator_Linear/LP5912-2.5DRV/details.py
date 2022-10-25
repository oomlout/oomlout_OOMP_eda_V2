
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LP5912-2.5DRV"
    hexID = "SZKREGULATORLINEARLP591225DRV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LP5912-0.9DRV', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LP5912-2.5DRV', 'kicadSymbolFootprint': 'Package_SON:WSON-6-1EP_2x2mm_P0.65mm_EP1x1.6mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lp5912.pdf', 'kicadSymbolki_keywords': 'Single Output LDO Low-Noise', 'kicadSymbolki_description': '500-mA Ultra-Low-Noise Low-IQ LDO, 2.5V, WSON-6', 'kicadSymbolki_fp_filters': 'WSON*1EP*2x2mm*P0.65mm*'}])
    newPart['name'].append('Regulator_Linear : LP5912-2.5DRV')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

