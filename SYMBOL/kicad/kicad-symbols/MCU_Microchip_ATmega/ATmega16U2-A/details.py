
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATmega"
    oIndex = "ATmega16U2-A"
    hexID = "SZKMCUMCHIPATMEGAATMEGA16U2A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATmega8U2-A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATmega16U2-A', 'kicadSymbolFootprint': 'Package_QFP:TQFP-32_7x7mm_P0.8mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/doc7799.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller MegaAVR', 'kicadSymbolki_description': '16MHz, 16kB Flash, 512B SRAM, 512B EEPROM, TQFP-32', 'kicadSymbolki_fp_filters': 'TQFP*7x7mm*P0.8mm*'}])
    newPart['name'].append('MCU_Microchip_ATmega : ATmega16U2-A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

