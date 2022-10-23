
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATmega"
    oIndex = "ATxmega128A1-C7"
    hexID = "SZKMCUMCHIPATMEGAATXMEGA128A1C7"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATxmega64A1-C7', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATxmega128A1-C7', 'kicadSymbolFootprint': 'Package_BGA:VFBGA-100_7.0x7.0mm_Layout10x10_P0.65mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8067-8-and-16-bit-AVR-Microcontrollers-ATxmega64A1-ATxmega128A1_Datasheet.pdf', 'kicadSymbolki_keywords': 'AVR 8/16bit Microcontroller XMegaAVR', 'kicadSymbolki_description': '32MHz, 128kB Flash, 8kB Boot, 8kB SRAM, 2kB EEPROM, JTAG, VFBGA-100', 'kicadSymbolki_fp_filters': 'VFBGA*7.0x7.0mm*Layout10x10*P0.65mm*'}])
    newPart['name'].append('ATxmega128A1-C7')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

