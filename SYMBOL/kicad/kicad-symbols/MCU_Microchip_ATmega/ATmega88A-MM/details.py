
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATmega"
    oIndex = "ATmega88A-MM"
    hexID = "SZKMCUMCHIPATMEGAATMEGA88A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATmega48PV-10MM', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATmega88A-MM', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-28-1EP_4x4mm_P0.45mm_EP2.4x2.4mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/ATmega48A_88A_168A-Data-Sheet-40002007A.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller MegaAVR', 'kicadSymbolki_description': '20MHz, 8kB Flash, 1kB SRAM, 512B EEPROM, QFN-28', 'kicadSymbolki_fp_filters': 'QFN*1EP*4x4mm*P0.45mm*'}])
    newPart['name'].append('MCU_Microchip_ATmega : ATmega88A-MM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

