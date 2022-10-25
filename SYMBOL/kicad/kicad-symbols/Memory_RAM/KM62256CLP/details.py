
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_RAM"
    oIndex = "KM62256CLP"
    hexID = "SZKMEMORYRAMKM62256CLP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'KM62256CLP', 'kicadSymbolFootprint': 'Package_DIP:DIP-28_W15.24mm', 'kicadSymbolDatasheet': 'https://www.futurlec.com/Datasheet/Memory/62256.pdf', 'kicadSymbolki_keywords': 'RAM SRAM CMOS MEMORY', 'kicadSymbolki_description': '32Kx8 bit Low Power CMOS Static RAM, 55/70ns, DIP-28', 'kicadSymbolki_fp_filters': 'DIP*W15.24mm*'}])
    newPart['name'].append('Memory_RAM : KM62256CLP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

