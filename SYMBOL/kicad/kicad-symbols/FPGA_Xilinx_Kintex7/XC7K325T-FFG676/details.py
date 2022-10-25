
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Xilinx_Kintex7"
    oIndex = "XC7K325T-FFG676"
    hexID = "SZKFPGAXILINXKINTEX7XC7K325TFFG676"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XC7K325T-FFG676', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'FPGA', 'kicadSymbolki_description': 'Kintex 7 T 325 XC7K325T-FFG676'}])
    newPart['name'].append('FPGA_Xilinx_Kintex7 : XC7K325T-FFG676')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

