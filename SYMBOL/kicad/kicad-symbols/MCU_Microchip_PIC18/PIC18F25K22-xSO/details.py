
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC18"
    oIndex = "PIC18F25K22-xSO"
    hexID = "SZKMCUMCHIPPIC18PIC18F25K22XSO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC18F23K22-xSO', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC18F25K22-xSO', 'kicadSymbolFootprint': 'Package_SO:SOIC-28W_7.5x17.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/40001412G.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8-Bit Microcontroller XLP', 'kicadSymbolki_description': '32K Flash, 1536B SRAM, 256B EEPROM, nanoWatt XLP, 2.3V to 5.5V, SOIC28', 'kicadSymbolki_fp_filters': 'SO*W*7.5x17.9mm*P1.27mm*'}])
    newPart['name'].append('MCU_Microchip_PIC18 : PIC18F25K22-xSO')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

