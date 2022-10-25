
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F1517-IMV"
    hexID = "SZKMCUMCHIPPIC16PIC16F1517IMV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16F1517-IMV', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/41452B.pdf', 'kicadSymbolki_keywords': 'FLASH-Based 8-Bit CMOS Microcontroller XLP', 'kicadSymbolki_description': 'PIC16F1517, 8192W FLASH, 512B SRAM, UQFN-40', 'kicadSymbolki_fp_filters': 'UQFN*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F1517-IMV')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

