
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATmega"
    oIndex = "ATmega48A-CC"
    hexID = "SZKMCUMCHIPATMEGAATMEGA48ACC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATmega48A-CC', 'kicadSymbolFootprint': 'Package_BGA:UFBGA-32_4.0x4.0mm_Layout6x6_P0.5mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/ATmega48A_88A_168A-Data-Sheet-40002007A.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller MegaAVR', 'kicadSymbolki_description': '20MHz, 4kB Flash, 512B SRAM, 256B EEPROM, UFBGA-32', 'kicadSymbolki_fp_filters': 'UFBGA*4.0x4.0mm*Layout6x6*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_ATmega : ATmega48A-CC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

