
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Xilinx_Spartan6"
    oIndex = "XC6SLX45-FGG484"
    hexID = "SZKFPGAXILINXSPARTAN6XC6SLX45FGG484"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XC6SLX45-FGG484', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'FPGA', 'kicadSymbolki_description': 'Spartan 6 LX 45 XC6SLX45-FGG484'}])
    newPart['name'].append('FPGA_Xilinx_Spartan6 : XC6SLX45-FGG484')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

