
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC18"
    oIndex = "PIC18LF24K50-xSO"
    hexID = "SZKMCUMCHIPPIC18PIC18LF24K5XSO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC18F24K50-xSO', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC18LF24K50-xSO', 'kicadSymbolFootprint': 'Package_SO:SOIC-28W_7.5x17.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/30000684B.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8-Bit Microcontroller XLP', 'kicadSymbolki_description': '16K Flash, 2K SRAM, 256 EEPROM, USB, nanoWatt XLP, 1.8V to 3.6V, SOIC28', 'kicadSymbolki_fp_filters': 'SO*W*7.5x17.9mm*P1.27mm*'}])
    newPart['name'].append('MCU_Microchip_PIC18 : PIC18LF24K50-xSO')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

