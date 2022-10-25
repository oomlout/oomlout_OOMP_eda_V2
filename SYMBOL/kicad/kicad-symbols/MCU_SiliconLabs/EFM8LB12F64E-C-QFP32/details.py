
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_SiliconLabs"
    oIndex = "EFM8LB12F64E-C-QFP32"
    hexID = "SZKMCUSILICONLABSEFM8LB12F64ECQFP32"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'EFM8LB12F32E-C-QFP32', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EFM8LB12F64E-C-QFP32', 'kicadSymbolFootprint': 'Package_QFP:LQFP-32_7x7mm_P0.8mm', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/efm8lb1-datasheet.pdf', 'kicadSymbolki_keywords': '8051 microcontroller', 'kicadSymbolki_description': '8051-compatible microcontroller, 72 MHz, 2.2 to 3.6V, 64K flash, 2304B RAM, -40 to +105 C, QFP-32', 'kicadSymbolki_fp_filters': 'LQFP*7x7mm*P0.8mm*'}])
    newPart['name'].append('MCU_SiliconLabs : EFM8LB12F64E-C-QFP32')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

