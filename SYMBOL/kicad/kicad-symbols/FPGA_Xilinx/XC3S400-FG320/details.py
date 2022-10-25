
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Xilinx"
    oIndex = "XC3S400-FG320"
    hexID = "SZKFPGAXILINXXC3S4FG32"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XC3S400-FG320', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': ''}])
    newPart['name'].append('FPGA_Xilinx : XC3S400-FG320')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

