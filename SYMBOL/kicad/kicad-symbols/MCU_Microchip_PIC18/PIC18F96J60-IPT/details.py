
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC18"
    oIndex = "PIC18F96J60-IPT"
    hexID = "SZKMCUMCHIPPIC18PIC18F96J6IPT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC18F96J60-IPT', 'kicadSymbolFootprint': 'Package_QFP:TQFP-100_12x12mm_P0.4mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/39762f.pdf', 'kicadSymbolki_keywords': 'Flash Based 8-Bit Microcontroller Ethernet Controller PHY', 'kicadSymbolki_description': '64K Flash, 3.7K SRAM, Ethernet Controller with PHY, 8K Buffer, TQFP100', 'kicadSymbolki_fp_filters': 'TQFP*12x12mm*P0.4mm* TQFP*14x14mm*P0.5mm*'}])
    newPart['name'].append('PIC18F96J60-IPT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

