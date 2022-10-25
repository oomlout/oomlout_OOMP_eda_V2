
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATtiny"
    oIndex = "ATtiny4313-M"
    hexID = "SZKMCUMCHIPATTINYATTINY4313M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATtiny2313V-10M', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATtiny4313-M', 'kicadSymbolFootprint': 'Package_DFN_QFN:MLF-20-1EP_4x4mm_P0.5mm_EP2.6x2.6mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/doc8246.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller tinyAVR', 'kicadSymbolki_description': '20MHz, 4kB Flash, 256B SRAM, 256B EEPROM, QFN-20', 'kicadSymbolki_fp_filters': 'MLF*1EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_ATtiny : ATtiny4313-M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

