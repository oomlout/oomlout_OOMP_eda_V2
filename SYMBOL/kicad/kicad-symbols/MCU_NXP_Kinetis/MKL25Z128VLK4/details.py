
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_Kinetis"
    oIndex = "MKL25Z128VLK4"
    hexID = "SZKMCUNXPKINETISMKL25Z128VLK4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MKL25Z128VLK4', 'kicadSymbolFootprint': 'Package_QFP:LQFP-80_12x12mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/docs/en/data-sheet/KL25P80M48SF0.pdf', 'kicadSymbolki_keywords': 'Kinetis KL25 ARM Cortex M0+', 'kicadSymbolki_description': 'Kinetis KL25 series, 48-MHz/32-bit ARM Cortex-M0+, 128 kB flash, 16 kB SRAM, USB FS Device/OTG, LQFP-80', 'kicadSymbolki_fp_filters': 'LQFP*12x12mm*P0.5mm*'}])
    newPart['name'].append('MKL25Z128VLK4')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

