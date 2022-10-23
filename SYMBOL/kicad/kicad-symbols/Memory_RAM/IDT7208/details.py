
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_RAM"
    oIndex = "IDT7208"
    hexID = "SZKMEMORYRAMIDT728"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IDT7204', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IDT7208', 'kicadSymbolFootprint': 'Package_DIP:DIP-28_W7.62mm', 'kicadSymbolDatasheet': 'http://www.idt.com/document/7203-7208-datasheet', 'kicadSymbolki_keywords': 'asynchronous fifo memory', 'kicadSymbolki_description': '65536x9 CMOS Asynchronous FIFO, DIP-28', 'kicadSymbolki_fp_filters': 'DIP*7.62mm*'}])
    newPart['name'].append('IDT7208')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

