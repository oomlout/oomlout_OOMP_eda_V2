
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Dialog"
    oIndex = "DA14691"
    hexID = "SZKMCUDIALOGDA14691"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DA14691', 'kicadSymbolFootprint': 'Package_BGA:VFBGA-86_6x6mm_Layout10x10_P0.55mm_Ball0.25mm_Pad0.2mm', 'kicadSymbolDatasheet': 'https://www.dialog-semiconductor.com/sites/default/files/da1469x_datasheet_3v1.pdf', 'kicadSymbolki_keywords': 'BLE MCU', 'kicadSymbolki_description': 'Multi-core BLE 5.1 SoC series, 96-MHz/32-bit ARM Cortex-M33, 128 kB ROM, 384 kB SRAM, 4 kB OTP Memory, 16 kB cache SRAM, VFBGA-86', 'kicadSymbolki_fp_filters': 'VFBGA*6x6mm*Layout10x10*P0.55mm*'}])
    newPart['name'].append('MCU_Dialog : DA14691')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

