
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F628A-ISS"
    hexID = "SZKMCUMCHIPPIC16PIC16F628AISS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC16F627A-ISS', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16F628A-ISS', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/40044G.pdf', 'kicadSymbolki_keywords': 'FLASH-Based 8-Bit CMOS Microcontroller', 'kicadSymbolki_description': 'PIC16F628A, 2048W Flash, 224B SRAM, 128B EEPROM, SSOP20', 'kicadSymbolki_fp_filters': 'SSOP*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F628A-ISS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

