
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "CPLD_Xilinx"
    oIndex = "XCR3064-VQ100"
    hexID = "SZKCPLDXILINXXCR364VQ1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'XCR3064XL-VQ100', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XCR3064-VQ100', 'kicadSymbolFootprint': 'Package_QFP:LQFP-100_14x14mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.xilinx.com/support/documentation/data_sheets/ds017.pdf', 'kicadSymbolki_keywords': 'CPLD', 'kicadSymbolki_description': 'Xilinx CoolRunner 64-Macrocell CPLD, 3.3V, VQFP-100, Obsolete', 'kicadSymbolki_fp_filters': 'LQFP*14x14mm*P0.5*'}])
    newPart['name'].append('XCR3064-VQ100')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

