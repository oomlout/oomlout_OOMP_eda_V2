
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "DRV8833RTY"
    hexID = "SZKDRIVERMOTORDRV8833RTY"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DRV8833RTY', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_S-PWQFN-N16_EP2.1x2.1mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/drv8833.pdf', 'kicadSymbolki_keywords': 'H-bridge motor driver', 'kicadSymbolki_description': 'Dual H-Bridge Motor Driver, WQFN-16', 'kicadSymbolki_fp_filters': 'Texas*S?PWQFN?N*EP*'}])
    newPart['name'].append('Driver_Motor : DRV8833RTY')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

