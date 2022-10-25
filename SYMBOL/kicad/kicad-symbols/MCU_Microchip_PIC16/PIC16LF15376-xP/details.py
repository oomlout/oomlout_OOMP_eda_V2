
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16LF15376-xP"
    hexID = "SZKMCUMCHIPPIC16PIC16LF15376XP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC16F15375-xP', 'kicadSymbolReference': 'U?', 'kicadSymbolValue': 'PIC16LF15376-xP', 'kicadSymbolFootprint': 'Package_DIP:DIP-40_W15.24mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/PIC16LF15356-75-76-85-86-Data%20Sheet-40001866B.pdf', 'kicadSymbolki_keywords': 'FLASH-Based 8-Bit CMOS Microcontroller Low Power', 'kicadSymbolki_description': '16KW FLASH, 2048B SRAM, DIP-40', 'kicadSymbolki_fp_filters': 'DIP*15.24mm*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16LF15376-xP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

