
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_Kinetis"
    oIndex = "MKL43Z128VLH4"
    hexID = "SZKMCUNXPKINETISMKL43Z128VLH4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MKL43Z256VLH4', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MKL43Z128VLH4', 'kicadSymbolFootprint': 'Package_QFP:LQFP-64_10x10mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/docs/en/data-sheet/KL43P64M48SF6.pdf', 'kicadSymbolki_keywords': 'Kinetis KL43 ARM Cortex M0+', 'kicadSymbolki_description': 'Kinetis KL43 series, 48-MHz/32-bit ARM Cortex-M0+, 128 kB flash, 16 kB SRAM, USB FS Device (xtal-less), Segment LCD, FlexIO, LQFP-64', 'kicadSymbolki_fp_filters': 'LQFP*10x10mm*P0.5mm*'}])
    newPart['name'].append('MCU_NXP_Kinetis : MKL43Z128VLH4')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

