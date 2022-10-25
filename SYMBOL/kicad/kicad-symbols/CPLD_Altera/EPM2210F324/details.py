
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "CPLD_Altera"
    oIndex = "EPM2210F324"
    hexID = "SZKCPLDALTERAEPM221F324"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EPM2210F324', 'kicadSymbolFootprint': 'Package_BGA:BGA-324_19.0x19.0mm_Layout18x18_P1.0mm_Ball0.5mm_Pad0.4mm_NSMD', 'kicadSymbolDatasheet': 'https://www.altera.com/content/dam/altera-www/global/en_US/pdfs/literature/hb/max2/max2_mii5v1.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'MAX2 FBGA', 'kicadSymbolki_description': 'Altera MAX2 CPLD with 2210 LE', 'kicadSymbolki_fp_filters': '*BGA*P1.0mm*'}])
    newPart['name'].append('CPLD_Altera : EPM2210F324')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

