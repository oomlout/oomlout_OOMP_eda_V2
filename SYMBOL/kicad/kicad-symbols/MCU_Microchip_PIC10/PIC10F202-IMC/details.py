
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC10"
    oIndex = "PIC10F202-IMC"
    hexID = "SZKMCUMCHIPPIC1PIC1F22IMC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC10F200-IMC', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC10F202-IMC', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_2x3mm_P0.5mm_EP0.61x2.2mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/41239D.pdf', 'kicadSymbolki_keywords': 'FLASH 8-Bit CMOS Microcontroller', 'kicadSymbolki_description': '512W Flash, 24B SRAM, DFN8', 'kicadSymbolki_fp_filters': 'DFN*8*1EP*2x3mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_PIC10 : PIC10F202-IMC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

