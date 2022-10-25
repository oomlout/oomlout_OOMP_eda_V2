
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F18855-xMV"
    hexID = "SZKMCUMCHIPPIC16PIC16F18855XMV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16F18855-xMV', 'kicadSymbolFootprint': 'Package_DFN_QFN:UQFN-28-1EP_4x4mm_P0.4mm_EP2.35x2.35mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/PIC16LF18855-75-Data-Sheet-40001802F.pdf', 'kicadSymbolki_keywords': 'FLASH-Based 8-Bit CMOS Microcontroller Low Power CRC DSM  ADC^2 CLC PLL 32MHz', 'kicadSymbolki_description': '8-bit Flash MCU, 32MHz, 14KB Flash, 1KB RAM 256B EEPROM, UQFN-28', 'kicadSymbolki_fp_filters': 'UQFN*1EP*4x4mm*P0.4mm*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F18855-xMV')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

