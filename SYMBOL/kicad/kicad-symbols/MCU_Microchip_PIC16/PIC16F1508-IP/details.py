
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F1508-IP"
    hexID = "SZKMCUMCHIPPIC16PIC16F158IP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16F1508-IP', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/41609A.pdf', 'kicadSymbolki_keywords': 'FLASH-Based 8-Bit CMOS Microcontroller XLP', 'kicadSymbolki_description': '4096W FLASH, 256B SRAM, PDIP-20', 'kicadSymbolki_fp_filters': 'DIP* PDIP* SO* SSOP*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F1508-IP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

