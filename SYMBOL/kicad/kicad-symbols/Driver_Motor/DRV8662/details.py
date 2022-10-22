
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "DRV8662"
    hexID = "SZKDRIVERMOTORDRV8662"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DRV8662', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_S-PVQFN-N20_EP2.7x2.7mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/drv8662.pdf', 'kicadSymbolki_keywords': 'piezo driver boost', 'kicadSymbolki_description': 'Piezo Haptic Driver with Integrated Boost Converter', 'kicadSymbolki_fp_filters': 'Texas*S*PVQFN*EP2.7x2.7mm*ThermalVias*'}])
    newPart['name'].append('DRV8662')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

