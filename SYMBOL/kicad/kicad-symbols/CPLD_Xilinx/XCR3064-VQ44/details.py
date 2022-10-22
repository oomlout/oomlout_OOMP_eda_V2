
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "CPLD_Xilinx"
    oIndex = "XCR3064-VQ44"
    hexID = "SZKCPLDXILINXXCR364VQ44"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'XCR3064XL-VQ44', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XCR3064-VQ44', 'kicadSymbolFootprint': 'Package_QFP:LQFP-44_10x10mm_P0.8mm', 'kicadSymbolDatasheet': 'https://www.xilinx.com/support/documentation/data_sheets/ds017.pdf', 'kicadSymbolki_keywords': 'CPLD', 'kicadSymbolki_description': 'Xilinx CoolRunner 64-Macrocell CPLD, 3.3V, VQFP-44, Obsolete', 'kicadSymbolki_fp_filters': 'LQFP*10x10mm*P0.8mm*'}])
    newPart['name'].append('XCR3064-VQ44')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

