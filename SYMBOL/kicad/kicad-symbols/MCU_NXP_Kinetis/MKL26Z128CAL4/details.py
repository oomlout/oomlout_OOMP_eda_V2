
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_Kinetis"
    oIndex = "MKL26Z128CAL4"
    hexID = "SZKMCUNXPKINETISMKL26Z128CAL4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MKL26Z128CAL4', 'kicadSymbolFootprint': 'Package_CSP:WLCSP-36_2.374x2.459mm_Layout6x6_P0.35mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/docs/en/data-sheet/KL26P36M48SF5.pdf', 'kicadSymbolki_keywords': 'Kinetis KL26 ARM Cortex M0+', 'kicadSymbolki_description': 'Kinetis KL26 series, 48-MHz/32-bit ARM Cortex-M0+, 128 kB flash, 16 kB SRAM, USB FS Device/OTG, WLCSP-36', 'kicadSymbolki_fp_filters': 'WLCSP*2.374x2.459mm*P0.35mm*'}])
    newPart['name'].append('MCU_NXP_Kinetis : MKL26Z128CAL4')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

