
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "CPLD_Xilinx"
    oIndex = "XC9536PC44"
    hexID = "SZKCPLDXILINXXC9536PC44"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XC9536PC44', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'xilinx/xc9536.pdf', 'kicadSymbolki_description': 'Xilinx CPLD, Obsolete'}])
    newPart['name'].append('CPLD_Xilinx : XC9536PC44')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

