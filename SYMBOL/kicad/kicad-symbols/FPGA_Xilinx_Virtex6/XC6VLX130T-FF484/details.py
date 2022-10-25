
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Xilinx_Virtex6"
    oIndex = "XC6VLX130T-FF484"
    hexID = "SZKFPGAXILINXVIRTEX6XC6VLX13TFF484"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XC6VLX130T-FF484', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'FPGA', 'kicadSymbolki_description': 'Virtex 6 LXT 130 XC6VLX130T-FF484'}])
    newPart['name'].append('FPGA_Xilinx_Virtex6 : XC6VLX130T-FF484')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

