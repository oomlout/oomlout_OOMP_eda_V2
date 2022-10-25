
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Xilinx_Virtex7"
    oIndex = "XC7V585T-FFG1157"
    hexID = "SZKFPGAXILINXVIRTEX7XC7V585TFFG1157"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XC7V585T-FFG1157', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'FPGA', 'kicadSymbolki_description': 'Virtex 7 T 585 XC7V585T-FFG1157'}])
    newPart['name'].append('FPGA_Xilinx_Virtex7 : XC7V585T-FFG1157')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

