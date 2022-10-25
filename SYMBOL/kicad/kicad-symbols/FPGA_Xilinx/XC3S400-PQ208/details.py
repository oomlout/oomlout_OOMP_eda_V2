
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Xilinx"
    oIndex = "XC3S400-PQ208"
    hexID = "SZKFPGAXILINXXC3S4PQ28"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XC3S400-PQ208', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': ''}])
    newPart['name'].append('FPGA_Xilinx : XC3S400-PQ208')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

