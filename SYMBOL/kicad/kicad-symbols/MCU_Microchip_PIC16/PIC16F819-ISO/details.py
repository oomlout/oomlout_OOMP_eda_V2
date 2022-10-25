
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F819-ISO"
    hexID = "SZKMCUMCHIPPIC16PIC16F819ISO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC16F818-ISO', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16F819-ISO', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/39598F.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8-Bit Microcontroller nanoWatt', 'kicadSymbolki_description': 'PIC16F819, 3584B Flash, 256B SRAM, 256B EEPROM, ADC, SOIC18', 'kicadSymbolki_fp_filters': 'SO*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F819-ISO')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

