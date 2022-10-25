
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16LF15385-xMV"
    hexID = "SZKMCUMCHIPPIC16PIC16LF15385XMV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC16F15386-xMV', 'kicadSymbolReference': 'U?', 'kicadSymbolValue': 'PIC16LF15385-xMV', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-48-1EP_6x6mm_P0.4mm_EP4.6x4.6mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/PIC16LF15356-75-76-85-86-Data%20Sheet-40001866B.pdf', 'kicadSymbolki_keywords': 'FLASH-Based 8-Bit CMOS Microcontroller Low Power', 'kicadSymbolki_description': '8KW FLASH, 1024B SRAM, QFN-48(6x6mm)', 'kicadSymbolki_fp_filters': 'QFN*6x6mm*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16LF15385-xMV')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

