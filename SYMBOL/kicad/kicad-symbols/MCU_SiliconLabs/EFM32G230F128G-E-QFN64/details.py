
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_SiliconLabs"
    oIndex = "EFM32G230F128G-E-QFN64"
    hexID = "SZKMCUSILICONLABSEFM32G23F128GEQFN64"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EFM32G230F128G-E-QFN64', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-64-1EP_9x9mm_P0.5mm_EP7.3x7.3mm', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/efm32g-datasheet.pdf', 'kicadSymbolki_keywords': 'MCU microcontroller silicon labs siliconlabs silabs EFM32 gecko', 'kicadSymbolki_description': '32-bit ARM Cortex-M3 microcontroller, 128 kB flash, 16 kB x 8 RAM, Silicon Labs - Gecko, QFN-64', 'kicadSymbolki_fp_filters': 'QFN*1EP*9x9mm*P0.5mm*'}])
    newPart['name'].append('EFM32G230F128G-E-QFN64')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

