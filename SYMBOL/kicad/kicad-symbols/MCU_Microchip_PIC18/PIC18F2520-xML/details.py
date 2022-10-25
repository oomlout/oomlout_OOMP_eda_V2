
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC18"
    oIndex = "PIC18F2520-xML"
    hexID = "SZKMCUMCHIPPIC18PIC18F252XML"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC18F2420-xML', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC18F2520-xML', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-28-1EP_6x6mm_P0.65mm_EP4.25x4.25mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/39631E.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8bit CMOS Microcontroller', 'kicadSymbolki_description': 'MCU 32k Flash, 1536B SRAM, 256B EEPROM, ADC, QFN-28', 'kicadSymbolki_fp_filters': 'QFN*1EP*6x6mm*P0.65mm*'}])
    newPart['name'].append('MCU_Microchip_PIC18 : PIC18F2520-xML')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

