
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_Flash"
    oIndex = "AM29PDL128G"
    hexID = "SZKMEMORYFLASHAM29PDL128G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AM29PDL128G', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_description': '128 Megabit (8 M x 16-Bit/4 M x 32-Bit), Simultaneous Operation Flash Memory with VersatileIO™ Control', 'kicadSymbolki_fp_filters': 'BGA80_1mm_15X10'}])
    newPart['name'].append('Memory_Flash : AM29PDL128G')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

