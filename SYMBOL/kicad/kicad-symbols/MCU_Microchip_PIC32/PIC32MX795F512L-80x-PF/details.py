
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC32"
    oIndex = "PIC32MX795F512L-80x-PF"
    hexID = "SZKMCUMCHIPPIC32PIC32MX795F512L8XPF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC32MX795F512L-80x-PF', 'kicadSymbolFootprint': 'Package_QFP:TQFP-100_14x14mm_P0.5mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/60001156J.pdf', 'kicadSymbolki_keywords': '32-bit MIPS MCU Microcontroller', 'kicadSymbolki_description': 'MIPS MCU, 80MHz, 512KB Flash, 12KB Boot Flash, 128KB RAM, 2.3-3.6V, USB, CAN, Ethernet, TQFP-100', 'kicadSymbolki_fp_filters': 'TQFP*14x14mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_PIC32 : PIC32MX795F512L-80x-PF')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

