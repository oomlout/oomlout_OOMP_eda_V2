
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_Kinetis"
    oIndex = "MKL25Z32VLH4"
    hexID = "SZKMCUNXPKINETISMKL25Z32VLH4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MKL25Z128VLH4', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MKL25Z32VLH4', 'kicadSymbolFootprint': 'Package_QFP:LQFP-64_10x10mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/docs/en/data-sheet/KL25P80M48SF0.pdf', 'kicadSymbolki_keywords': 'Kinetis KL25 ARM Cortex M0+', 'kicadSymbolki_description': 'Kinetis KL25 series, 48-MHz/32-bit ARM Cortex-M0+, 32 kB flash, 4 kB SRAM, USB FS Device/OTG, LQFP-64', 'kicadSymbolki_fp_filters': 'LQFP*10x10mm*P0.5mm*'}])
    newPart['name'].append('MCU_NXP_Kinetis : MKL25Z32VLH4')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

