
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Haptic"
    oIndex = "DRV2510-Q1"
    hexID = "SZKDRIVERHAPTICDRV251Q1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DRV2510-Q1', 'kicadSymbolFootprint': 'Package_SO:HTSSOP-16-1EP_4.4x5mm_P0.65mm_EP3.4x5mm_Mask3x3mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/drv2510-q1.pdf', 'kicadSymbolki_keywords': 'driver haptic solenoid coil', 'kicadSymbolki_description': 'Haptic driver for solenoids and voice coils, up to 3A output, TSSOP-16', 'kicadSymbolki_fp_filters': 'HTSSOP*1EP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('DRV2510-Q1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

