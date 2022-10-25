
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "CPLD_Xilinx"
    oIndex = "XC95108PC84"
    hexID = "SZKCPLDXILINXXC9518PC84"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XC95108PC84', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'xilinx/xc95108.pdf', 'kicadSymbolki_description': 'Xilinx CPLD, Obsolete'}])
    newPart['name'].append('CPLD_Xilinx : XC95108PC84')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

