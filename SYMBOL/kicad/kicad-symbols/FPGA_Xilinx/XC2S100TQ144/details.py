
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Xilinx"
    oIndex = "XC2S100TQ144"
    hexID = "SZKFPGAXILINXXC2S1TQ144"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XC2S100TQ144', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'xilinx/spartan2e/spartan2e.pdf', 'kicadSymbolki_keywords': 'FPGA', 'kicadSymbolki_description': 'spartan 2'}])
    newPart['name'].append('FPGA_Xilinx : XC2S100TQ144')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

