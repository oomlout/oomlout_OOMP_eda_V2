
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATmega"
    oIndex = "ATmega3250P-20A"
    hexID = "SZKMCUMCHIPATMEGAATMEGA325P2A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATmega3250V-8A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATmega3250P-20A', 'kicadSymbolFootprint': 'Package_QFP:TQFP-100_14x14mm_P0.5mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/doc8023.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller MegaAVR', 'kicadSymbolki_description': '20MHz, 32kB Flash, 2kB SRAM, 1kB EEPROM, JTAG, TQFP-100', 'kicadSymbolki_fp_filters': 'TQFP*14x14mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_ATmega : ATmega3250P-20A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

