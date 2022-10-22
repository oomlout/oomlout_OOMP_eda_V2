
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "DRV8801RTY"
    hexID = "SZKDRIVERMOTORDRV881RTY"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DRV8801RTY', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_S-PWQFN-N16_EP2.1x2.1mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/drv8801.pdf', 'kicadSymbolki_keywords': 'H-Bridge Motor Driver', 'kicadSymbolki_description': 'H-Bridge Motor Driver, WQFN-16', 'kicadSymbolki_fp_filters': 'Texas*S?PWQFN?N*EP*'}])
    newPart['name'].append('DRV8801RTY')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

