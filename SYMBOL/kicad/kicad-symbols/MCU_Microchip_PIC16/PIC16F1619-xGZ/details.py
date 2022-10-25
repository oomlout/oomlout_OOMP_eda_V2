
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F1619-xGZ"
    hexID = "SZKMCUMCHIPPIC16PIC16F1619XGZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16F1619-xGZ', 'kicadSymbolFootprint': 'Package_DFN_QFN:UQFN-20-1EP_4x4mm_P0.5mm_EP2.8x2.8mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/40001770D.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8-Bit CMOS Microcontroller Low Power', 'kicadSymbolki_description': '8-bit Flash MCU, 32MHz, 14KB Flash, 1KB RAM, 1K High Endurance Flash (EEPROM), UQFN-20', 'kicadSymbolki_fp_filters': 'UQFN*1EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F1619-xGZ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

