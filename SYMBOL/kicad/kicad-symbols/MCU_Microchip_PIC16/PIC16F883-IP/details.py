
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F883-IP"
    hexID = "SZKMCUMCHIPPIC16PIC16F883IP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC16F882-IP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16F883-IP', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/41291D.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8-Bit CMOS Microcontroller', 'kicadSymbolki_description': '4K Flash, 256B SRAM, 256B EEPROM, XLP, DIP28', 'kicadSymbolki_fp_filters': 'DIP* PDIP*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F883-IP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

