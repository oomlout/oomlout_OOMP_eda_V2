
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F1619-xP"
    hexID = "SZKMCUMCHIPPIC16PIC16F1619XP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16F1619-xP', 'kicadSymbolFootprint': 'Package_DIP:DIP-20_W7.62mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/40001770D.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8-Bit CMOS Microcontroller Low Power', 'kicadSymbolki_description': '8-bit Flash MCU, 32MHz, 14KB Flash, 1KB RAM, 1K High Endurance Flash (EEPROM), PDIP-20', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F1619-xP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

