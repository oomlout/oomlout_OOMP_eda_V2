
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATmega"
    oIndex = "ATmega48A-A"
    hexID = "SZKMCUMCHIPATMEGAATMEGA48AA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATmega48PV-10A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATmega48A-A', 'kicadSymbolFootprint': 'Package_QFP:TQFP-32_7x7mm_P0.8mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/ATmega48A_88A_168A-Data-Sheet-40002007A.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller MegaAVR', 'kicadSymbolki_description': '20MHz, 4kB Flash, 512B SRAM, 256B EEPROM, TQFP-32', 'kicadSymbolki_fp_filters': 'TQFP*7x7mm*P0.8mm*'}])
    newPart['name'].append('MCU_Microchip_ATmega : ATmega48A-A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

