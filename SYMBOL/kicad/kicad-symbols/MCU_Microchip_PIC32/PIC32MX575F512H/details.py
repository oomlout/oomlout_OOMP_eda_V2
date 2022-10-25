
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC32"
    oIndex = "PIC32MX575F512H"
    hexID = "SZKMCUMCHIPPIC32PIC32MX575F512H"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC32MX575F256H', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC32MX575F512H', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/61156G.pdf', 'kicadSymbolki_keywords': 'Microchip PIC32 Microcontroller MIPS', 'kicadSymbolki_description': '32-bit Microcontrollers (64KB Flash and 16KB SRAM TQFP-64 QFN-64) USB, CAN and Ethernet', 'kicadSymbolki_fp_filters': 'Package*QFP:QFP*10x10mm*P0.5mm* Package*DFN*QFN:QFN*1EP*9x9mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_PIC32 : PIC32MX575F512H')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

