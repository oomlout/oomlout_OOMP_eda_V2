
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC18"
    oIndex = "PIC18LF24K50-xML"
    hexID = "SZKMCUMCHIPPIC18PIC18LF24K5XML"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC18F24K50-xML', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC18LF24K50-xML', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-28-1EP_6x6mm_P0.65mm_EP4.25x4.25mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/30000684B.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8-Bit Microcontroller XLP', 'kicadSymbolki_description': '16K Flash, 2K SRAM, 256 EEPROM, USB, nanoWatt XLP, 1.8V to 3.6V, QFN28', 'kicadSymbolki_fp_filters': 'QFN*1EP*6x6mm*P0.65mm*'}])
    newPart['name'].append('MCU_Microchip_PIC18 : PIC18LF24K50-xML')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

