
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC10"
    oIndex = "PIC10F200-IP"
    hexID = "SZKMCUMCHIPPIC1PIC1F2IP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC10F200-IP', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/41239D.pdf', 'kicadSymbolki_keywords': 'FLASH 8-Bit CMOS Microcontroller', 'kicadSymbolki_description': '256W Flash, 16B SRAM, PDIP8', 'kicadSymbolki_fp_filters': 'DIP*8*W7.62mm*'}])
    newPart['name'].append('MCU_Microchip_PIC10 : PIC10F200-IP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

