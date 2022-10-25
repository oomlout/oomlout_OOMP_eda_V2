
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATmega"
    oIndex = "ATmega48-20MM"
    hexID = "SZKMCUMCHIPATMEGAATMEGA482"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATmega48V-10MM', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATmega48-20MM', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-28-1EP_4x4mm_P0.45mm_EP2.4x2.4mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-2545-8-bit-AVR-Microcontroller-ATmega48-88-168_Datasheet.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller MegaAVR', 'kicadSymbolki_description': '20MHz, 4kB Flash, 512B SRAM, 256B EEPROM, QFN-28', 'kicadSymbolki_fp_filters': 'QFN*1EP*4x4mm*P0.45mm*'}])
    newPart['name'].append('MCU_Microchip_ATmega : ATmega48-20MM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

