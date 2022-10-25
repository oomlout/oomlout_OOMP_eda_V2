
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "CPLD_Altera"
    oIndex = "EPM570M100"
    hexID = "SZKCPLDALTERAEPM57M1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EPM570M100', 'kicadSymbolFootprint': 'Package_BGA:BGA-100_6.0x6.0mm_Layout11x11_P0.5mm_Ball0.3mm_Pad0.25mm_NSMD', 'kicadSymbolDatasheet': 'https://www.altera.com/content/dam/altera-www/global/en_US/pdfs/literature/hb/max2/max2_mii5v1.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'MAX2 MBGA', 'kicadSymbolki_description': 'Altera MAX2 CPLD with 570 LE', 'kicadSymbolki_fp_filters': '*BGA*P0.5mm*'}])
    newPart['name'].append('CPLD_Altera : EPM570M100')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

