
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_AVR_Dx"
    oIndex = "AVR64DA28x-xSP"
    hexID = "SZKMCUMCHIPAVRDXAVR64DA28XXSP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AVR32DA28x-xSO', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AVR64DA28x-xSP', 'kicadSymbolFootprint': 'Package_DIP:DIP-28_W7.62mm', 'kicadSymbolDatasheet': 'https://ww1.microchip.com/downloads/en/DeviceDoc/AVR64DA28-32-48-64-Data-Sheet-40002233B.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller AVR-DA', 'kicadSymbolki_description': '24MHz, 64kB Flash, 8kB SRAM, EEPROM with Touch Sensing, SPDIP-28', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('MCU_Microchip_AVR_Dx : AVR64DA28x-xSP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

