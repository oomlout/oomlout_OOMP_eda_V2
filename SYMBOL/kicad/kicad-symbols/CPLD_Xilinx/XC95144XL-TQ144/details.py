
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "CPLD_Xilinx"
    oIndex = "XC95144XL-TQ144"
    hexID = "SZKCPLDXILINXXC95144XLTQ144"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XC95144XL-TQ144', 'kicadSymbolFootprint': 'Package_QFP:TQFP-144_20x20mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.xilinx.com/support/documentation/data_sheets/ds056.pdf', 'kicadSymbolki_keywords': 'CPLD', 'kicadSymbolki_description': 'CPLD, 144 Macrocells, 3200 Usable Gates', 'kicadSymbolki_fp_filters': 'TQFP*20x20mm*P0.5mm*'}])
    newPart['name'].append('CPLD_Xilinx : XC95144XL-TQ144')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

