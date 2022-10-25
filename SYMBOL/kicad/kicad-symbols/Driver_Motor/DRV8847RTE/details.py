
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "DRV8847RTE"
    hexID = "SZKDRIVERMOTORDRV8847RTE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DRV8847RTE', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-16-1EP_3x3mm_P0.5mm_EP1.7x1.7mm_ThermalVias', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/drv8847.pdf', 'kicadSymbolki_keywords': 'Dual H-Bridge motor driver', 'kicadSymbolki_description': 'Dual H-Bridge Motor Driver, 1A, WQFN-16', 'kicadSymbolki_fp_filters': 'QFN*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Driver_Motor : DRV8847RTE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

