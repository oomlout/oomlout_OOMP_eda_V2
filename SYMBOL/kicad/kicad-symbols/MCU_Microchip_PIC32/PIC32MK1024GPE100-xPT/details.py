
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC32"
    oIndex = "PIC32MK1024GPE100-xPT"
    hexID = "SZKMCUMCHIPPIC32PIC32MK124GPE1XPT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC32MK1024GPD100-xPT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC32MK1024GPE100-xPT', 'kicadSymbolFootprint': 'Package_QFP:TQFP-100_12x12mm_P0.4mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/PIC32MK_GP_MC_Familly_Datasheet_60001402G.pdf', 'kicadSymbolki_keywords': '32-bit MIPS MCU Microcontroller', 'kicadSymbolki_description': 'MIPS MCU, 120MHz, 1MB Flash, 256KB RAM, 2.3-3.6V, USB, TQFP-100', 'kicadSymbolki_fp_filters': 'TQFP*12x12mm*P0.4mm*'}])
    newPart['name'].append('MCU_Microchip_PIC32 : PIC32MK1024GPE100-xPT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

