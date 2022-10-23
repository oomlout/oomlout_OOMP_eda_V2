
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC32"
    oIndex = "PIC32MX170F256D-IPT"
    hexID = "SZKMCUMCHIPPIC32PIC32MX17F256DIPT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC32MX110F016D-IPT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC32MX170F256D-IPT', 'kicadSymbolFootprint': 'Package_QFP:TQFP-44_10x10mm_P0.8mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/60001168F.pdf', 'kicadSymbolki_keywords': 'Microchip PIC32 Microcontroller MIPS', 'kicadSymbolki_description': '32-bit Microcontrollers (256KB Flash and 64KB SRAM TQFP-44) with Audio and Graphics Interfaces, USB, and Advanced Analog', 'kicadSymbolki_fp_filters': 'TQFP*10x10mm*P0.8mm*'}])
    newPart['name'].append('PIC32MX170F256D-IPT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

