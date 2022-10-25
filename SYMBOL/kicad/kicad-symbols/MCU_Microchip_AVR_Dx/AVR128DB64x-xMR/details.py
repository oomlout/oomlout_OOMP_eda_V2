
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_AVR_Dx"
    oIndex = "AVR128DB64x-xMR"
    hexID = "SZKMCUMCHIPAVRDXAVR128DB64XXMR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AVR64DB64x-xMR', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AVR128DB64x-xMR', 'kicadSymbolFootprint': 'Package_DFN_QFN:VQFN-64-1EP_9x9mm_P0.5mm_EP7.15x7.15mm', 'kicadSymbolDatasheet': 'https://ww1.microchip.com/downloads/en/DeviceDoc/AVR128DB28-32-48-64-DataSheet-DS40002247A.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller AVR-DB', 'kicadSymbolki_description': '24MHz, 128kB Flash, 16kB SRAM, EEPROM with Op Amps and Multi-Voltage I/O, VQFN-64', 'kicadSymbolki_fp_filters': 'VQFN*1EP*9x9mm*P0.5mm*EP7.15x7.15mm*'}])
    newPart['name'].append('MCU_Microchip_AVR_Dx : AVR128DB64x-xMR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

