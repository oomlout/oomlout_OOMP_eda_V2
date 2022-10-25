
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC12"
    oIndex = "PIC12F635-ISN"
    hexID = "SZKMCUMCHIPPIC12PIC12F635ISN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC12F635-IP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC12F635-ISN', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/41232D.pdf', 'kicadSymbolki_keywords': 'FLASH-Based 8-Bit CMOS Microcontroller', 'kicadSymbolki_description': 'PIC12F635, 1024W Flash, 64B SRAM, 128B EEPROM, SO8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('MCU_Microchip_PIC12 : PIC12F635-ISN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

