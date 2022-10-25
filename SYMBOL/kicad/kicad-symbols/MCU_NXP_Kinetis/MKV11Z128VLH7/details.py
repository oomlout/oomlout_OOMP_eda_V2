
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_Kinetis"
    oIndex = "MKV11Z128VLH7"
    hexID = "SZKMCUNXPKINETISMKV11Z128VLH7"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MKV11Z128VLH7', 'kicadSymbolFootprint': 'Package_QFP:LQFP-64_10x10mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/KV11P64M75.pdf', 'kicadSymbolki_keywords': 'Kinetis KV11 ARM Cortex M0+', 'kicadSymbolki_description': 'Kinetis KV11 series, 75-MHz/32-bit ARM Cortex-M0+, 128 kB flash, 16 kB RAM, Entry-Level, Real-time Motor Control, LQFP-64', 'kicadSymbolki_fp_filters': 'LQFP*10x10mm*P0.5mm*'}])
    newPart['name'].append('MCU_NXP_Kinetis : MKV11Z128VLH7')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

