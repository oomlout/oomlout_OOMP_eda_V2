
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC18"
    oIndex = "PIC18F452-IP"
    hexID = "SZKMCUMCHIPPIC18PIC18F452IP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC18F442-IP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC18F452-IP', 'kicadSymbolFootprint': 'Package_DIP:DIP-40_W15.24mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/39564c.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8-Bit Microcontroller', 'kicadSymbolki_description': '32K Flash, 1536B SRAM, 256 EEPROM, ADC, DIP40', 'kicadSymbolki_fp_filters': 'DIP*W15.24mm* PDIP*W15.24mm*'}])
    newPart['name'].append('MCU_Microchip_PIC18 : PIC18F452-IP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

