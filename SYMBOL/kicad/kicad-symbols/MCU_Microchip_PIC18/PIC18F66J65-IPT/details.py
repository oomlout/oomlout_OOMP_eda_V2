
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC18"
    oIndex = "PIC18F66J65-IPT"
    hexID = "SZKMCUMCHIPPIC18PIC18F66J65IPT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC18F66J60-IPT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC18F66J65-IPT', 'kicadSymbolFootprint': 'Package_QFP:TQFP-64_10x10mm_P0.5mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/39762f.pdf', 'kicadSymbolki_keywords': 'Flash Based 8-Bit Microcontroller Ethernet Controller PHY', 'kicadSymbolki_description': '96K Flash, 3.7K SRAM, Ethernet Controller with PHY, 8K Buffer, TQFP64', 'kicadSymbolki_fp_filters': 'TQFP*10x10mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_PIC18 : PIC18F66J65-IPT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

