
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "DRV8308"
    hexID = "SZKDRIVERMOTORDRV838"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DRV8308', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_S-PVQFN-N40_EP3.52x2.62mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/drv8308.pdf', 'kicadSymbolki_keywords': 'bldc mosfet-driver hall-sensor', 'kicadSymbolki_description': 'Brushless DC motor controller, closed loop, hall sensor inputs, current limiting, SPI interface', 'kicadSymbolki_fp_filters': 'Texas*S*PVQFN*N40*3.52x2.62mm*'}])
    newPart['name'].append('Driver_Motor : DRV8308')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

