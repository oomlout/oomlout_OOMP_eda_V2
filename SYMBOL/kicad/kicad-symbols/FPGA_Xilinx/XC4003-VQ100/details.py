
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Xilinx"
    oIndex = "XC4003-VQ100"
    hexID = "SZKFPGAXILINXXC43VQ1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XC4003-VQ100', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'xilinx/xc400x-pinout.pdf'}])
    newPart['name'].append('FPGA_Xilinx : XC4003-VQ100')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

