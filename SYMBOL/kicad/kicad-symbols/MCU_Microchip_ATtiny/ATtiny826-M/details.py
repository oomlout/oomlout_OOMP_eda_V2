
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATtiny"
    oIndex = "ATtiny826-M"
    hexID = "SZKMCUMCHIPATTINYATTINY826M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATtiny406-M', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATtiny826-M', 'kicadSymbolFootprint': 'Package_DFN_QFN:VQFN-20-1EP_3x3mm_P0.4mm_EP1.7x1.7mm', 'kicadSymbolDatasheet': 'https://ww1.microchip.com/downloads/en/DeviceDoc/ATtiny424-426-427-824-826-827-DataSheet-DS40002311A.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller tinyAVR', 'kicadSymbolki_description': '20MHz, 8kB Flash, 1kB SRAM, 128B EEPROM, VQFN-20', 'kicadSymbolki_fp_filters': 'VQFN*1EP*3x3mm*P0.4mm*'}])
    newPart['name'].append('MCU_Microchip_ATtiny : ATtiny826-M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

