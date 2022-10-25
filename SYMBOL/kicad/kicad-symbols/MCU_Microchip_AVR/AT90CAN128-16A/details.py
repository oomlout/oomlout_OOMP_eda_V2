
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_AVR"
    oIndex = "AT90CAN128-16A"
    hexID = "SZKMCUMCHIPAVRAT9CAN12816A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AT90CAN32-16A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AT90CAN128-16A', 'kicadSymbolFootprint': 'Package_QFP:TQFP-64_14x14mm_P0.8mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/doc7679.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller MegaAVR', 'kicadSymbolki_description': '16MHz, 128kB Flash, 4kB SRAM, 4kB EEPROM, JTAG, CAN, TQFP-64', 'kicadSymbolki_fp_filters': 'TQFP*14x14mm*P0.8mm*'}])
    newPart['name'].append('MCU_Microchip_AVR : AT90CAN128-16A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

