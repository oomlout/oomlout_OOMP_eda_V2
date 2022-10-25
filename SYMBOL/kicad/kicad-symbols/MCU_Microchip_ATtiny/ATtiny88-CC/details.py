
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATtiny"
    oIndex = "ATtiny88-CC"
    hexID = "SZKMCUMCHIPATTINYATTINY88CC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATtiny48-CC', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATtiny88-CC', 'kicadSymbolFootprint': 'Package_BGA:UFBGA-32_4.0x4.0mm_Layout6x6_P0.5mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/doc8008.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller tinyAVR', 'kicadSymbolki_description': '12MHz, 8kB Flash, 512B SRAM, 64B EEPROM, UFBGA-32', 'kicadSymbolki_fp_filters': 'UFBGA*4.0x4.0mm*Layout6x6*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_ATtiny : ATtiny88-CC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

