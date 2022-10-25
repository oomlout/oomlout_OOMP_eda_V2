
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC18"
    oIndex = "PIC18F2550-ISO"
    hexID = "SZKMCUMCHIPPIC18PIC18F255ISO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC18F2455-ISO', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC18F2550-ISO', 'kicadSymbolFootprint': 'Package_SO:SOIC-28W_7.5x17.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/39632c.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8-Bit Microcontroller XLP', 'kicadSymbolki_description': '32K Flash, 2K SRAM, 256 EEPROM, USB, nanoWatt XLP, SOIC28', 'kicadSymbolki_fp_filters': 'SO*W*7.5x17.9mm_P1.27mm*'}])
    newPart['name'].append('MCU_Microchip_PIC18 : PIC18F2550-ISO')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

