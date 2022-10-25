
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC24"
    oIndex = "PIC24FJ256DA210-xBG"
    hexID = "SZKMCUMCHIPPIC24PIC24FJ256DA21XBG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC24FJ256DA210-xBG', 'kicadSymbolFootprint': 'Package_BGA:XBGA-121_10x10mm_Layout11x11_P0.8mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/39969b.pdf', 'kicadSymbolki_keywords': 'Flash-Based 16-Bit Microcontroller', 'kicadSymbolki_description': '256K Flash, 96KB SRAM, Graphic controller, USB, BGA-121', 'kicadSymbolki_fp_filters': 'XBGA*10x10mm*Layout11x11*P0.8mm*'}])
    newPart['name'].append('MCU_Microchip_PIC24 : PIC24FJ256DA210-xBG')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

