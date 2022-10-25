
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F687-ISO"
    hexID = "SZKMCUMCHIPPIC16PIC16F687ISO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16F687-ISO', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/41262E.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8-Bit CMOS Microcontroller nanoWatt', 'kicadSymbolki_description': 'PIC16F687, 2048W Flash, 128B SRAM, 256B EEPROM, SO20', 'kicadSymbolki_fp_filters': 'SO*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F687-ISO')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

