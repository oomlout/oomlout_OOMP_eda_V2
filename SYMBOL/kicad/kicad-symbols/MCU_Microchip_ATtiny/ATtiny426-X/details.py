
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATtiny"
    oIndex = "ATtiny426-X"
    hexID = "SZKMCUMCHIPATTINYATTINY426X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATtiny406-S', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATtiny426-X', 'kicadSymbolFootprint': 'Package_SO:SSOP-20_5.3x7.2mm_P0.65mm', 'kicadSymbolDatasheet': 'https://ww1.microchip.com/downloads/en/DeviceDoc/ATtiny424-426-427-824-826-827-DataSheet-DS40002311A.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller tinyAVR', 'kicadSymbolki_description': '20MHz, 4kB Flash, 512B SRAM, 128B EEPROM, SSOP-20', 'kicadSymbolki_fp_filters': 'SSOP*5.3x7.2mm*P0.65mm*'}])
    newPart['name'].append('MCU_Microchip_ATtiny : ATtiny426-X')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

