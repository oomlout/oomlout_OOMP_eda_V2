
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATmega"
    oIndex = "ATmega3208-X"
    hexID = "SZKMCUMCHIPATMEGAATMEGA328X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATmega3208-X', 'kicadSymbolFootprint': 'Package_SO:SSOP-28_5.3x10.2mm_P0.65mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/40002018A.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller MegaAVR', 'kicadSymbolki_description': '20MHz, 32kB Flash, 4kB SRAM, 256B EEPROM, SSOP-28', 'kicadSymbolki_fp_filters': 'SSOP*5.3x10.2mm*P0.65mm*'}])
    newPart['name'].append('MCU_Microchip_ATmega : ATmega3208-X')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

