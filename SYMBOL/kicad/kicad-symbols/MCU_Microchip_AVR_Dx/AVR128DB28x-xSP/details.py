
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_AVR_Dx"
    oIndex = "AVR128DB28x-xSP"
    hexID = "SZKMCUMCHIPAVRDXAVR128DB28XXSP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AVR32DB28x-xSO', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AVR128DB28x-xSP', 'kicadSymbolFootprint': 'Package_DIP:DIP-28_W7.62mm', 'kicadSymbolDatasheet': 'https://ww1.microchip.com/downloads/en/DeviceDoc/AVR128DB28-32-48-64-DataSheet-DS40002247A.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller AVR-DB', 'kicadSymbolki_description': '24MHz, 128kB Flash, 16kB SRAM, EEPROM with Op Amps and Multi-Voltage I/O, SPDIP-28', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('MCU_Microchip_AVR_Dx : AVR128DB28x-xSP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

