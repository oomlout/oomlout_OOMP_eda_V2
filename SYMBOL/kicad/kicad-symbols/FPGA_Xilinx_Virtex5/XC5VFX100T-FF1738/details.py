
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Xilinx_Virtex5"
    oIndex = "XC5VFX100T-FF1738"
    hexID = "SZKFPGAXILINXVIRTEX5XC5VFX1TFF1738"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XC5VFX100T-FF1738', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'FPGA', 'kicadSymbolki_description': 'Virtex 5 FXT 100 XC5VFX100T-FF1738'}])
    newPart['name'].append('FPGA_Xilinx_Virtex5 : XC5VFX100T-FF1738')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

