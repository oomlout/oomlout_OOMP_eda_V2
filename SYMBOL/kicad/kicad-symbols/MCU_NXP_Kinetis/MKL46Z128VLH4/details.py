
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_Kinetis"
    oIndex = "MKL46Z128VLH4"
    hexID = "SZKMCUNXPKINETISMKL46Z128VLH4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MKL46Z256VLH4', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MKL46Z128VLH4', 'kicadSymbolFootprint': 'Package_QFP:LQFP-64_10x10mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/docs/en/data-sheet/KL46P121M48SF4.pdf', 'kicadSymbolki_keywords': 'Kinetis KL46 ARM Cortex M0+', 'kicadSymbolki_description': 'Kinetis KL46 series, 48-MHz/32-bit ARM Cortex-M0+, 128 kB flash, 16 kB SRAM, USB FS Device/OTG, Segment LCD, TSI, LQFP-64', 'kicadSymbolki_fp_filters': 'LQFP*10x10mm*P0.5mm*'}])
    newPart['name'].append('MCU_NXP_Kinetis : MKL46Z128VLH4')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

