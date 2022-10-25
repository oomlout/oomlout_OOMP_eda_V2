
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC18"
    oIndex = "PIC18F87K22-xPT"
    hexID = "SZKMCUMCHIPPIC18PIC18F87K22XPT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC18F87K22-xPT', 'kicadSymbolFootprint': 'Package_QFP:TQFP-80_12x12mm_P0.5mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/39960d.pdf', 'kicadSymbolki_keywords': 'Flash Based 8-Bit Microcontroller', 'kicadSymbolki_description': 'PIC18F nanoWatt XLP Technology MCU, 64MHz, 128KB Flash, 4KB RAM, 1KB EEPROM, 1.8-5.5V, 69 GPIO, TQFP-80', 'kicadSymbolki_fp_filters': 'TQFP*12x12mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_PIC18 : PIC18F87K22-xPT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

