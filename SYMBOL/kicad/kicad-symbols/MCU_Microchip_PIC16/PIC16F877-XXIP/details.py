
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F877-XXIP"
    hexID = "SZKMCUMCHIPPIC16PIC16F877XXIP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC16F874-XXIP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16F877-XXIP', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/30292C.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8-Bit CMOS Microcontroller', 'kicadSymbolki_description': 'PIC16F877, 8K Flash, 386B SRAM, 256B EEPROM, DIP40', 'kicadSymbolki_fp_filters': 'DIP* PDIP*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F877-XXIP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

