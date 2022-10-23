
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Xilinx"
    oIndex = "XC2C256-VQ100"
    hexID = "SZKFPGAXILINXXC2C256VQ1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XC2C256-VQ100', 'kicadSymbolFootprint': 'Package_QFP:VQFP-100_14x14mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.xilinx.com/support/documentation/data_sheets/ds094.pdf', 'kicadSymbolki_keywords': 'CPLD', 'kicadSymbolki_description': 'CoolRunner-II CPLD, 256 macrocells, VQFP-100', 'kicadSymbolki_fp_filters': 'VQFP*14x14mm*P0.5mm*'}])
    newPart['name'].append('XC2C256-VQ100')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

