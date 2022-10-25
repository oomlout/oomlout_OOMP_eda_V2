
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC12"
    oIndex = "PIC12C508-IJW"
    hexID = "SZKMCUMCHIPPIC12PIC12C58IJW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC12C508-IP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC12C508-IJW', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/40139e.pdf', 'kicadSymbolki_keywords': '8-Bit CMOS Microcontroller', 'kicadSymbolki_description': 'PIC12C508, 512W EPROM, 25B SRAM, CERDIP8 Windowed', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('MCU_Microchip_PIC12 : PIC12C508-IJW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

