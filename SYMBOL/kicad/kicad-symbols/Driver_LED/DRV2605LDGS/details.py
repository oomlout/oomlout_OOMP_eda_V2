
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_LED"
    oIndex = "DRV2605LDGS"
    hexID = "SZKDRIVERLDRV265LDGS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DRV2605LDGS', 'kicadSymbolFootprint': 'Package_SO:VSSOP-10_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/drv2605l.pdf', 'kicadSymbolki_keywords': 'haptic driver i2c', 'kicadSymbolki_description': 'Haptic driver for LRAs and ERMs with effect library, 2-5.2V, VSSOP-10', 'kicadSymbolki_fp_filters': 'VSSOP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Driver_LED : DRV2605LDGS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

