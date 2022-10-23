
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATmega"
    oIndex = "ATxmega32A4U-C"
    hexID = "SZKMCUMCHIPATMEGAATXMEGA32A4UC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATxmega16A4U-C', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATxmega32A4U-C', 'kicadSymbolFootprint': 'Package_BGA:VFBGA-49_5.0x5.0mm_Layout7x7_P0.65mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8387-8-and16-bit-AVR-Microcontroller-XMEGA-A4U_Datasheet.pdf', 'kicadSymbolki_keywords': 'AVR 8/16bit Microcontroller XMegaAVR', 'kicadSymbolki_description': '32MHz, 32kB Flash, 4kB Boot, 4kB SRAM, 1kB EEPROM, JTAG, USB, VFBGA-49', 'kicadSymbolki_fp_filters': 'VFBGA*5.0x5.0mm*Layout7x7*P0.65mm*'}])
    newPart['name'].append('ATxmega32A4U-C')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

