
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC18"
    oIndex = "PIC18LF4480-IP"
    hexID = "SZKMCUMCHIPPIC18PIC18LF448IP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC18F4580-IP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC18LF4480-IP', 'kicadSymbolFootprint': 'Package_DIP:DIP-40_W15.24mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/39637d.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8-Bit Microcontroller CAN', 'kicadSymbolki_description': '32K Flash, 768B SRAM, 256 EEPROM, ECAN, DIP40', 'kicadSymbolki_fp_filters': 'DIP*W15.24mm* PDIP*W15.24mm*'}])
    newPart['name'].append('MCU_Microchip_PIC18 : PIC18LF4480-IP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

