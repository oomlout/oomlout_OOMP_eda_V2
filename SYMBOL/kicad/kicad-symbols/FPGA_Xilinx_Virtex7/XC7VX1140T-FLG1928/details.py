
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Xilinx_Virtex7"
    oIndex = "XC7VX1140T-FLG1928"
    hexID = "SZKFPGAXILINXVIRTEX7XC7VX114TFLG1928"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XC7VX1140T-FLG1928', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'FPGA', 'kicadSymbolki_description': 'Virtex 7 XT 1140 XC7VX1140T-FLG1928'}])
    newPart['name'].append('FPGA_Xilinx_Virtex7 : XC7VX1140T-FLG1928')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

