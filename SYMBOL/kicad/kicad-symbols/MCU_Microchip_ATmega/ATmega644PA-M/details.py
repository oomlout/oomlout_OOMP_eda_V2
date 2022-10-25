
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATmega"
    oIndex = "ATmega644PA-M"
    hexID = "SZKMCUMCHIPATMEGAATMEGA644PAM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATmega164A-M', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATmega644PA-M', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-44-1EP_7x7mm_P0.5mm_EP5.2x5.2mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8272-8-bit-AVR-microcontroller-ATmega164A_PA-324A_PA-644A_PA-1284_P_datasheet.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller MegaAVR PicoPower', 'kicadSymbolki_description': '20MHz, 64kB Flash, 4kB SRAM, 2kB EEPROM, JTAG, QFN-44', 'kicadSymbolki_fp_filters': 'QFN*1EP*7x7mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_ATmega : ATmega644PA-M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

