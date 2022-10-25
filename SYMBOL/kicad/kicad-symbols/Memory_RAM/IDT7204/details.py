
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_RAM"
    oIndex = "IDT7204"
    hexID = "SZKMEMORYRAMIDT724"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IDT7204', 'kicadSymbolFootprint': 'Package_DIP:DIP-28_W7.62mm', 'kicadSymbolDatasheet': 'http://www.idt.com/document/7203-7208-datasheet', 'kicadSymbolki_keywords': 'asynchronous fifo memory', 'kicadSymbolki_description': '4096x9 CMOS Asynchronous FIFO, DIP-28', 'kicadSymbolki_fp_filters': 'DIP*7.62mm*'}])
    newPart['name'].append('Memory_RAM : IDT7204')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

