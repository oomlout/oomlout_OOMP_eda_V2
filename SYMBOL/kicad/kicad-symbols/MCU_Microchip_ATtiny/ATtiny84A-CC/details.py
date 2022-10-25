
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATtiny"
    oIndex = "ATtiny84A-CC"
    hexID = "SZKMCUMCHIPATTINYATTINY84ACC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATtiny24A-CC', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATtiny84A-CC', 'kicadSymbolFootprint': 'Package_BGA:UFBGA-15_3.0x3.0mm_Layout4x4_P0.65mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/doc8183.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller tinyAVR', 'kicadSymbolki_description': '20MHz, 8kB Flash, 512B SRAM, 512B EEPROM, debugWIRE, UFBGA-15', 'kicadSymbolki_fp_filters': 'UFBGA*3.0x3.0mm*Layout4x4*P0.65mm*'}])
    newPart['name'].append('MCU_Microchip_ATtiny : ATtiny84A-CC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

