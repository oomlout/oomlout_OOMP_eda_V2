
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC18"
    oIndex = "PIC18F2420-xSP"
    hexID = "SZKMCUMCHIPPIC18PIC18F242XSP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC18F2420-xSP', 'kicadSymbolFootprint': 'Package_DIP:DIP-28_W15.24mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/39631E.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8bit CMOS Microcontroller', 'kicadSymbolki_description': 'MCU 16k Flash, 768B SRAM, 256B EEPROM, ADC, DIP-28', 'kicadSymbolki_fp_filters': 'DIP*W15.24mm*'}])
    newPart['name'].append('MCU_Microchip_PIC18 : PIC18F2420-xSP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

