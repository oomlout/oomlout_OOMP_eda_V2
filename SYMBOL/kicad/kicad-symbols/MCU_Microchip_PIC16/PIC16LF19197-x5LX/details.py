
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16LF19197-x5LX"
    hexID = "SZKMCUMCHIPPIC16PIC16LF19197X5LX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC16F19195-x5LX', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16LF19197-x5LX', 'kicadSymbolFootprint': 'Package_DFN_QFN:VQFN-64-1EP_9x9mm_P0.5mm_EP5.4x5.4mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/PIC16LF19195-6-7-Data-Sheet-40001873D.pdf', 'kicadSymbolki_keywords': 'FLASH-Based 8-Bit CMOS Microcontroller Low Power', 'kicadSymbolki_description': '32kW FLASH, 4kB RAM, 256B EEPROM, VQFN-64', 'kicadSymbolki_fp_filters': 'VQFN*9x9mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16LF19197-x5LX')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

