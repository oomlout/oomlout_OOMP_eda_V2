
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Xilinx"
    oIndex = "XC4005-PC84"
    hexID = "SZKFPGAXILINXXC45PC84"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'XC4003-PC84', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XC4005-PC84', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': ''}])
    newPart['name'].append('FPGA_Xilinx : XC4005-PC84')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

