
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "CPLD_Xilinx"
    oIndex = "XC9572XL-TQ100"
    hexID = "SZKCPLDXILINXXC9572XLTQ1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XC9572XL-TQ100', 'kicadSymbolFootprint': 'Package_QFP:TQFP-100_14x14mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.xilinx.com/support/documentation/data_sheets/ds057.pdf', 'kicadSymbolki_keywords': 'CPLD', 'kicadSymbolki_description': 'CPLD, 72 Macrocells, 1600 Usable Gates', 'kicadSymbolki_fp_filters': 'TQFP*14x14mm*P0.5mm*'}])
    newPart['name'].append('CPLD_Xilinx : XC9572XL-TQ100')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

