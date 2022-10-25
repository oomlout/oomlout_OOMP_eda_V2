
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F628-xxISO"
    hexID = "SZKMCUMCHIPPIC16PIC16F628XXISO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC16F627-xxISO', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16F628-xxISO', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/40300c.pdf', 'kicadSymbolki_keywords': 'FLASH-Based 8-Bit CMOS Microcontroller', 'kicadSymbolki_description': '2048W Flash, 224B SRAM, 128B EEPROM, SO18', 'kicadSymbolki_fp_filters': 'SO*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F628-xxISO')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

