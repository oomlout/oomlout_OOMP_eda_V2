
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F627A-ISS"
    hexID = "SZKMCUMCHIPPIC16PIC16F627AISS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16F627A-ISS', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/40044G.pdf', 'kicadSymbolki_keywords': 'FLASH-Based 8-Bit CMOS Microcontroller', 'kicadSymbolki_description': 'PIC16F627A, 1024W Flash, 224B SRAM, 128B EEPROM, SSOP20', 'kicadSymbolki_fp_filters': 'SSOP*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F627A-ISS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

