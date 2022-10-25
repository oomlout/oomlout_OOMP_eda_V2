
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_RAM"
    oIndex = "AS6C4008-55PCN"
    hexID = "SZKMEMORYRAMAS6C4855PCN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AS6C4008-55PCN', 'kicadSymbolFootprint': 'Package_DIP:DIP-32_W15.24mm', 'kicadSymbolDatasheet': 'https://www.alliancememory.com/wp-content/uploads/pdf/AS6C4008.pdf', 'kicadSymbolki_keywords': 'RAM SRAM CMOS MEMORY', 'kicadSymbolki_description': '512K x 8 Low Power CMOS RAM, DIP-32', 'kicadSymbolki_fp_filters': 'DIP*W15.24mm*'}])
    newPart['name'].append('Memory_RAM : AS6C4008-55PCN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

