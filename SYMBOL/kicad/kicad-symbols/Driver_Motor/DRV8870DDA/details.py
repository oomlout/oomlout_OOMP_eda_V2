
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "DRV8870DDA"
    hexID = "SZKDRIVERMOTORDRV887DDA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DRV8870DDA', 'kicadSymbolFootprint': 'Package_SO:Texas_HTSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.95x4.9mm_Mask2.4x3.1mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/drv8870.pdf', 'kicadSymbolki_keywords': 'H-bridge driver motor current limit', 'kicadSymbolki_description': 'Brushed DC Motor Driver, PWM Control, 45V, 3.6A, Dynamic current limiting, HTSOP-8', 'kicadSymbolki_fp_filters': 'Texas*HTSOP*1EP*3.9x4.9mm*P1.27mm*EP2.95x4.9mm*Mask2.4x3.1mm*'}])
    newPart['name'].append('DRV8870DDA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

