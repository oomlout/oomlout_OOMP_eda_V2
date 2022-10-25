
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC12"
    oIndex = "PIC12F629-IMS"
    hexID = "SZKMCUMCHIPPIC12PIC12F629IMS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC12F629-IP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC12F629-IMS', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/41190G.pdf', 'kicadSymbolki_keywords': 'FLASH-Based 8-Bit CMOS Microcontroller', 'kicadSymbolki_description': '1024W Flash, 64B SRAM, 128B EEPROM, PDIP8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('MCU_Microchip_PIC12 : PIC12F629-IMS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

