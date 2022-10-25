
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC24"
    oIndex = "PIC24FJ256DA210-xPT"
    hexID = "SZKMCUMCHIPPIC24PIC24FJ256DA21XPT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC24FJ256DA210-xPT', 'kicadSymbolFootprint': 'Package_QFP:TQFP-100_12x12mm_P0.4mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/39969b.pdf', 'kicadSymbolki_keywords': 'Flash-Based 16-Bit Microcontroller', 'kicadSymbolki_description': '256K Flash, 96KB SRAM, Graphic controller, USB, TQFP-100', 'kicadSymbolki_fp_filters': 'TQFP*12x12mm*P0.4mm*'}])
    newPart['name'].append('MCU_Microchip_PIC24 : PIC24FJ256DA210-xPT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

