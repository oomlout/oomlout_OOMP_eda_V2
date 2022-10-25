
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATmega"
    oIndex = "ATmega169P-16M"
    hexID = "SZKMCUMCHIPATMEGAATMEGA169P16M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATmega169PV-8M', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATmega169P-16M', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-64-1EP_9x9mm_P0.5mm_EP5.4x5.4mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/doc8018.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller MegaAVR LCD PicoPower', 'kicadSymbolki_description': '16MHz, 16kB Flash, 1kB SRAM, 512B EEPROM, QFN-64', 'kicadSymbolki_fp_filters': 'QFN*1EP*9x9mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_ATmega : ATmega169P-16M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

