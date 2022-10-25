
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F1527-IMR"
    hexID = "SZKMCUMCHIPPIC16PIC16F1527IMR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC16F1527-IPT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16F1527-IMR', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/41458B.pdf', 'kicadSymbolki_keywords': 'FLASH-Based 8-Bit CMOS Microcontroller XLP', 'kicadSymbolki_description': 'PIC16F1527, 16384W FLASH, 1536B SRAM, UQFN-64', 'kicadSymbolki_fp_filters': 'TQFP* QFN*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F1527-IMR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

