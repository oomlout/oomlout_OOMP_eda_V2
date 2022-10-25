
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC18"
    oIndex = "PIC18LF14K50-ESS"
    hexID = "SZKMCUMCHIPPIC18PIC18LF14K5ESS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC18F13K50-ESS', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC18LF14K50-ESS', 'kicadSymbolFootprint': 'Package_SO:SSOP-20_5.3x7.2mm_P0.65mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/41350c.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8bit CMOS Microcontroller XLP', 'kicadSymbolki_description': '16K Flash, 768 SRAM, 256 EEPROM, USB, nanoWatt XLP, SSOP20', 'kicadSymbolki_fp_filters': 'SSOP*5.3x7.2mm*P0.65mm*'}])
    newPart['name'].append('MCU_Microchip_PIC18 : PIC18LF14K50-ESS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

