
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "DRV8848"
    hexID = "SZKDRIVERMOTORDRV8848"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DRV8848', 'kicadSymbolFootprint': 'Package_SO:TSSOP-16-1EP_4.4x5mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/drv8848.pdf', 'kicadSymbolki_keywords': 'Dual H-Bridge motor driver', 'kicadSymbolki_description': 'Dual H-Bridge motor driver, PWM controlled, single/dual brushed DC stepper, +2 to +18 VDD, TSSOP-16', 'kicadSymbolki_fp_filters': 'TSSOP*1EP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('DRV8848')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

