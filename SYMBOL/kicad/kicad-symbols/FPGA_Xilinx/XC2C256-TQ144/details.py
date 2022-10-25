
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Xilinx"
    oIndex = "XC2C256-TQ144"
    hexID = "SZKFPGAXILINXXC2C256TQ144"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XC2C256-TQ144', 'kicadSymbolFootprint': 'Package_QFP:TQFP-144_20x20mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.xilinx.com/support/documentation/data_sheets/ds094.pdf', 'kicadSymbolki_keywords': 'CPLD', 'kicadSymbolki_description': 'CoolRunner-II CPLD, 256 macrocells', 'kicadSymbolki_fp_filters': 'TQFP*20x20mm*P0.5mm*'}])
    newPart['name'].append('FPGA_Xilinx : XC2C256-TQ144')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

