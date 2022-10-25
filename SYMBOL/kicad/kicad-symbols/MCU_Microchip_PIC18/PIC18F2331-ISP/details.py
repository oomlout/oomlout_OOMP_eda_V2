
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC18"
    oIndex = "PIC18F2331-ISP"
    hexID = "SZKMCUMCHIPPIC18PIC18F2331ISP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC18F2331-ISP', 'kicadSymbolFootprint': 'Package_DIP:DIP-28_W7.62mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/39616d.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8-Bit Microcontroller XLP', 'kicadSymbolki_description': '8K Flash, 768B SRAM, 256B EEPROM, nanoWatt XLP, ADC, PWM, SPDIP28', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* PDIP*W7.62mm*'}])
    newPart['name'].append('MCU_Microchip_PIC18 : PIC18F2331-ISP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

