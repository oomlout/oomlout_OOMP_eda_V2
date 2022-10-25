
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16LF18325-xGZ"
    hexID = "SZKMCUMCHIPPIC16PIC16LF18325XGZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC16F18325-xGZ', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16LF18325-xGZ', 'kicadSymbolFootprint': 'Package_DFN_QFN:UQFN-20-1EP_4x4mm_P0.5mm_EP2.8x2.8mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/40001795E.pdf', 'kicadSymbolki_keywords': 'FLASH-Based 8-Bit CMOS Microcontroller Low Power', 'kicadSymbolki_description': '8192W FLASH, 1024B SRAM, 256B EEPROM, QFN-20', 'kicadSymbolki_fp_filters': 'UQFN*1EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16LF18325-xGZ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

