
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_RaspberryPi"
    oIndex = "RP2040"
    hexID = "SZKMCURASPBERRYPIRP24"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'RP2040', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-56-1EP_7x7mm_P0.4mm_EP3.2x3.2mm', 'kicadSymbolDatasheet': 'https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf', 'kicadSymbolki_keywords': 'RP2040 ARM Cortex-M0+ USB', 'kicadSymbolki_description': 'A microcontroller by Raspberry Pi', 'kicadSymbolki_fp_filters': 'QFN*7x7mm?P0.4mm?EP3.2x3.2mm*'}])
    newPart['name'].append('MCU_RaspberryPi : RP2040')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

