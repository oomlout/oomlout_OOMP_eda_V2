
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "DRV8837C"
    hexID = "SZKDRIVERMOTORDRV8837C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DRV8837C', 'kicadSymbolFootprint': 'Package_SON:WSON-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/drv8837c.pdf', 'kicadSymbolki_keywords': 'half bridge driver', 'kicadSymbolki_description': 'H-Bridge driver, 1A, Low Voltage, PWM input, WSON-8', 'kicadSymbolki_fp_filters': 'WSON*1EP*2x2mm*P0.5mm*'}])
    newPart['name'].append('Driver_Motor : DRV8837C')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

