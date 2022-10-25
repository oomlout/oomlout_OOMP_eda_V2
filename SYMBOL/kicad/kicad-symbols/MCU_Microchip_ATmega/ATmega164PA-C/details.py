
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATmega"
    oIndex = "ATmega164PA-C"
    hexID = "SZKMCUMCHIPATMEGAATMEGA164PAC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATmega164A-C', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATmega164PA-C', 'kicadSymbolFootprint': 'Package_BGA:VFBGA-49_5.0x5.0mm_Layout7x7_P0.65mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8272-8-bit-AVR-microcontroller-ATmega164A_PA-324A_PA-644A_PA-1284_P_datasheet.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller MegaAVR PicoPower', 'kicadSymbolki_description': '20MHz, 16kB Flash, 1kB SRAM, 512B EEPROM, JTAG, VFBGA-49', 'kicadSymbolki_fp_filters': 'VFBGA*5.0x5.0mm*Layout7x7*P0.65mm*'}])
    newPart['name'].append('MCU_Microchip_ATmega : ATmega164PA-C')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

