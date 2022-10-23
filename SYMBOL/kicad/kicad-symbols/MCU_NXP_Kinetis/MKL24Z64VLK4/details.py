
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_Kinetis"
    oIndex = "MKL24Z64VLK4"
    hexID = "SZKMCUNXPKINETISMKL24Z64VLK4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MKL24Z64VLK4', 'kicadSymbolFootprint': 'Package_QFP:LQFP-80_12x12mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/docs/en/data-sheet/KL24P80M48SF0.pdf', 'kicadSymbolki_keywords': 'Kinetis KL24 ARM Cortex M0+', 'kicadSymbolki_description': 'Kinetis KL24 series, 48-MHz/32-bit ARM Cortex-M0+, 64 kB flash, 8 kB SRAM, USB FS Device/OTG, LQFP-80', 'kicadSymbolki_fp_filters': 'LQFP*12x12mm*P0.5mm*'}])
    newPart['name'].append('MKL24Z64VLK4')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

