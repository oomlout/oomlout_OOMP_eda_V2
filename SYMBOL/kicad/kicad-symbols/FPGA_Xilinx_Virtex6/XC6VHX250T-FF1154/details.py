
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Xilinx_Virtex6"
    oIndex = "XC6VHX250T-FF1154"
    hexID = "SZKFPGAXILINXVIRTEX6XC6VHX25TFF1154"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XC6VHX250T-FF1154', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'FPGA', 'kicadSymbolki_description': 'Virtex 6 HXT 250 XC6VHX250T-FF1154'}])
    newPart['name'].append('FPGA_Xilinx_Virtex6 : XC6VHX250T-FF1154')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

