
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "CPLD_Xilinx"
    oIndex = "XCR3128XL-VQ100"
    hexID = "SZKCPLDXILINXXCR3128XLVQ1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XCR3128XL-VQ100', 'kicadSymbolFootprint': 'Package_QFP:LQFP-100_14x14mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.xilinx.com/support/documentation/data_sheets/ds016.pdf', 'kicadSymbolki_keywords': 'CPLD', 'kicadSymbolki_description': 'Xilinx CoolRunner 128-Macrocell CPLD, 3.3V, VQFP-100', 'kicadSymbolki_fp_filters': 'LQFP*14x14mm*P0.5*'}])
    newPart['name'].append('CPLD_Xilinx : XCR3128XL-VQ100')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

