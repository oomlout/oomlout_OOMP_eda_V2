
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATmega"
    oIndex = "ATmega324PA-MC"
    hexID = "SZKMCUMCHIPATMEGAATMEGA324PAMC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATmega164A-MC', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATmega324PA-MC', 'kicadSymbolFootprint': 'Package_DFN_QFN:Microchip_DRQFN-44-1EP_5x5mm_P0.7mm_EP2.65x2.65mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8272-8-bit-AVR-microcontroller-ATmega164A_PA-324A_PA-644A_PA-1284_P_datasheet.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller MegaAVR', 'kicadSymbolki_description': '20MHz, 32kB Flash, 2kB SRAM, 1kB EEPROM, JTAG, DRQFN-44', 'kicadSymbolki_fp_filters': 'Microchip*DRQFN*1EP*5x5mm*P0.7mm*'}])
    newPart['name'].append('ATmega324PA-MC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

