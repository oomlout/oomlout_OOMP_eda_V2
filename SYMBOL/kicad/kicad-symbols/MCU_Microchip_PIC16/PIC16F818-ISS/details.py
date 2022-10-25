
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F818-ISS"
    hexID = "SZKMCUMCHIPPIC16PIC16F818ISS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16F818-ISS', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/39598F.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8-Bit Microcontroller nanoWatt', 'kicadSymbolki_description': 'PIC16F818, 1792B Flash, 128B SRAM, 128B EEPROM, ADC, SSSOP20', 'kicadSymbolki_fp_filters': 'SSOP*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F818-ISS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

