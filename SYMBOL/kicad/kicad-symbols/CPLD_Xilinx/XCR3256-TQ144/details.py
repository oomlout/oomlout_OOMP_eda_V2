
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "CPLD_Xilinx"
    oIndex = "XCR3256-TQ144"
    hexID = "SZKCPLDXILINXXCR3256TQ144"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'XCR3256XL-TQ144', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XCR3256-TQ144', 'kicadSymbolFootprint': 'Package_QFP:TQFP-144_20x20mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.xilinx.com/support/documentation/data_sheets/ds013.pdf', 'kicadSymbolki_keywords': 'CPLD', 'kicadSymbolki_description': 'Xilinx CoolRunner 256-Macrocell CPLD, 3.3V, TQFP-144, Obsolete', 'kicadSymbolki_fp_filters': 'TQFP*20x20mm*P0.5*'}])
    newPart['name'].append('CPLD_Xilinx : XCR3256-TQ144')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

