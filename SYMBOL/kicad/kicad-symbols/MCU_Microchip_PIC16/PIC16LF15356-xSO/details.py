
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16LF15356-xSO"
    hexID = "SZKMCUMCHIPPIC16PIC16LF15356XSO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC16F15356-xSO', 'kicadSymbolReference': 'U?', 'kicadSymbolValue': 'PIC16LF15356-xSO', 'kicadSymbolFootprint': 'Package_SO:SOIC-28W_7.5x17.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/PIC16LF15356-75-76-85-86-Data%20Sheet-40001866B.pdf', 'kicadSymbolki_keywords': 'FLASH-Based 8-Bit CMOS Microcontroller Low Power', 'kicadSymbolki_description': '16KW FLASH, 2048B SRAM, SOIC-28', 'kicadSymbolki_fp_filters': 'SOIC*.5x17.9mm*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16LF15356-xSO')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

