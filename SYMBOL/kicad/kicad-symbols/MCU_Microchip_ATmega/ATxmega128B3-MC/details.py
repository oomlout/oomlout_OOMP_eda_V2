
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATmega"
    oIndex = "ATxmega128B3-MC"
    hexID = "SZKMCUMCHIPATMEGAATXMEGA128B3MC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATxmega128B3-MC', 'kicadSymbolFootprint': 'Package_DFN_QFN:Microchip_DRQFN-64-1EP_7x7mm_P0.65mm_EP4.1x4.1mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8074-8-and-16-bit-AVR-Microcontroller-XMEGA-B-ATxmega64B3-ATxmega128B3_Datasheet.pdf', 'kicadSymbolki_keywords': 'AVR 8/16bit Microcontroller XMegaAVR', 'kicadSymbolki_description': '32MHz, 128kB Flash, 8kB Boot, 8kB SRAM, 2kB EEPROM, JTAG, USB, LCD, DRQFN-64', 'kicadSymbolki_fp_filters': 'Microchip*DRQFN*1EP*7x7mm*P0.65mm*'}])
    newPart['name'].append('ATxmega128B3-MC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

