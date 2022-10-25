
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F15356-xMV"
    hexID = "SZKMCUMCHIPPIC16PIC16F15356XMV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U?', 'kicadSymbolValue': 'PIC16F15356-xMV', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-28-1EP_4x4mm_P0.4mm_EP2.3x2.3mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/PIC16LF15356-75-76-85-86-Data%20Sheet-40001866B.pdf', 'kicadSymbolki_keywords': 'FLASH-Based 8-Bit CMOS Microcontroller Low Power', 'kicadSymbolki_description': '16KW FLASH, 2048B SRAM, QFN-28(4x4mm)', 'kicadSymbolki_fp_filters': 'QFN*4x4mm*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F15356-xMV')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

