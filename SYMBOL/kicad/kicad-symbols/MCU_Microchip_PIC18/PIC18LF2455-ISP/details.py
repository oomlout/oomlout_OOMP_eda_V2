
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC18"
    oIndex = "PIC18LF2455-ISP"
    hexID = "SZKMCUMCHIPPIC18PIC18LF2455ISP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC18F2455-ISP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC18LF2455-ISP', 'kicadSymbolFootprint': 'Package_DIP:DIP-28_W7.62mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/39632c.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8-Bit Microcontroller XLP', 'kicadSymbolki_description': '24K Flash, 2K SRAM, 256 EEPROM, USB, nanoWatt XLP, SPDIP28', 'kicadSymbolki_fp_filters': 'SPDIP*28_W7.62mm* DIP*28_W7.62mm* PDIP*28_W7.62mm*'}])
    newPart['name'].append('MCU_Microchip_PIC18 : PIC18LF2455-ISP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

