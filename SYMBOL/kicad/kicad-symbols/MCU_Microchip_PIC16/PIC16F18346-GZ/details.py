
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F18346-GZ"
    hexID = "SZKMCUMCHIPPIC16PIC16F18346GZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16F18346-GZ', 'kicadSymbolFootprint': 'Package_DFN_QFN:UQFN-20-1EP_4x4mm_P0.5mm_EP2.8x2.8mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/40001839B.pdf', 'kicadSymbolki_keywords': 'FLASH-Based 8-Bit CMOS Microcontroller Low Power', 'kicadSymbolki_description': '16384W FLASH, 2048B RAM, 256B EEPROM, UQFN-20', 'kicadSymbolki_fp_filters': '*UQFN*4x4mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F18346-GZ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

