
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Xilinx"
    oIndex = "XCV150_BG352"
    hexID = "SZKFPGAXILINXXCV15BG352"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XCV150_BG352', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.xilinx.com/support/documentation/data_sheets/ds003.pdf', 'kicadSymbolki_keywords': 'field programmable gate array', 'kicadSymbolki_description': 'Virtex FPGA'}])
    newPart['name'].append('XCV150_BG352')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

