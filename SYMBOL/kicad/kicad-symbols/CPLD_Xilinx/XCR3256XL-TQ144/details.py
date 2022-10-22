
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "CPLD_Xilinx"
    oIndex = "XCR3256XL-TQ144"
    hexID = "SZKCPLDXILINXXCR3256XLTQ144"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XCR3256XL-TQ144', 'kicadSymbolFootprint': 'Package_QFP:TQFP-144_20x20mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.xilinx.com/support/documentation/data_sheets/ds013.pdf', 'kicadSymbolki_keywords': 'CPLD', 'kicadSymbolki_description': 'Xilinx CoolRunner 256-Macrocell CPLD, 3.3V, TQFP-144', 'kicadSymbolki_fp_filters': 'TQFP*20x20mm*P0.5*'}])
    newPart['name'].append('XCR3256XL-TQ144')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

