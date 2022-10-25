
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "DRV8801PWP"
    hexID = "SZKDRIVERMOTORDRV881PWP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DRV8801PWP', 'kicadSymbolFootprint': 'Package_SO:HTSSOP-16-1EP_4.4x5mm_P0.65mm_EP3.4x5mm_Mask3x3mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/drv8801.pdf', 'kicadSymbolki_keywords': 'H-Bridge Motor Driver', 'kicadSymbolki_description': 'H-Bridge Motor Driver, TSSOP-16', 'kicadSymbolki_fp_filters': '*TSSOP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('Driver_Motor : DRV8801PWP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

