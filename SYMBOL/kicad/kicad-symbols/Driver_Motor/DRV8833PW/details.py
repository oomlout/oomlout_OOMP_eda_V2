
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "DRV8833PW"
    hexID = "SZKDRIVERMOTORDRV8833PW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DRV8833PW', 'kicadSymbolFootprint': 'Package_SO:TSSOP-16_4.4x5mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/drv8833.pdf', 'kicadSymbolki_keywords': 'H-bridge motor driver', 'kicadSymbolki_description': 'Dual H-Bridge Motor Driver, TSSOP-16', 'kicadSymbolki_fp_filters': 'TSSOP-16*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('Driver_Motor : DRV8833PW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

