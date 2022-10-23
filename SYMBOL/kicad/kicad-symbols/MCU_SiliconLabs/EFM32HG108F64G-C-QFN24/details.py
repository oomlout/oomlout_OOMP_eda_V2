
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_SiliconLabs"
    oIndex = "EFM32HG108F64G-C-QFN24"
    hexID = "SZKMCUSILICONLABSEFM32HG18F64GCQFN24"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'EFM32HG108F32G-C-QFN24', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EFM32HG108F64G-C-QFN24', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-24-1EP_5x5mm_P0.65mm_EP3.6x3.6mm', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/efm32hg-datasheet.pdf', 'kicadSymbolki_keywords': 'MCU microcontroller silicon labs siliconlabs silabs EFM32 happy gecko', 'kicadSymbolki_description': '32-bit ARM Cortex-M0 microcontroller, 64 kB flash, 4 kB  RAM, Silicon Labs - Happy Gecko, QFN-24', 'kicadSymbolki_fp_filters': 'QFN*1EP*5x5mm*P0.65mm*'}])
    newPart['name'].append('EFM32HG108F64G-C-QFN24')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

