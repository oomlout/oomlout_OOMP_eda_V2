
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC18"
    oIndex = "PIC18F24K50-xSP"
    hexID = "SZKMCUMCHIPPIC18PIC18F24K5XSP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC18F24K50-xSP', 'kicadSymbolFootprint': 'Package_DIP:DIP-28_W7.62mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/30000684B.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8-Bit Microcontroller XLP', 'kicadSymbolki_description': '16K Flash, 2K SRAM, 256 EEPROM, USB, nanoWatt XLP, 2.3V to 5.5V, SPDIP28', 'kicadSymbolki_fp_filters': 'SPDIP*W7.62mm* DIP*W7.62mm* PDIP*W7.62mm*'}])
    newPart['name'].append('MCU_Microchip_PIC18 : PIC18F24K50-xSP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

