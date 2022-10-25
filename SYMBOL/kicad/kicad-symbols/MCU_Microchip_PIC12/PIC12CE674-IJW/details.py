
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC12"
    oIndex = "PIC12CE674-IJW"
    hexID = "SZKMCUMCHIPPIC12PIC12CE674IJW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC12CE674-IP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC12CE674-IJW', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/30561b.pdf', 'kicadSymbolki_keywords': '8-Bit CMOS Microcontroller', 'kicadSymbolki_description': 'PIC12CE674, 2048W EPROM, 128B SRAM, 128B EEPROM, CERDIP8 Windowed', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('MCU_Microchip_PIC12 : PIC12CE674-IJW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

