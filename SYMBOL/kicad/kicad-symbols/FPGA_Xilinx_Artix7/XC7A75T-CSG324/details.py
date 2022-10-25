
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Xilinx_Artix7"
    oIndex = "XC7A75T-CSG324"
    hexID = "SZKFPGAXILINXARTIX7XC7A75TCSG324"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XC7A75T-CSG324', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'FPGA', 'kicadSymbolki_description': 'Artix 7 T 75 XC7A75T-CSG324'}])
    newPart['name'].append('FPGA_Xilinx_Artix7 : XC7A75T-CSG324')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

