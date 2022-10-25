
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_RAM"
    oIndex = "AS6C1616"
    hexID = "SZKMEMORYRAMAS6C1616"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AS6C1616', 'kicadSymbolFootprint': 'Package_SO:TSOP-I-48_18.4x12mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.alliancememory.com/wp-content/uploads/pdf/AS6C1616-TSOPI.pdf', 'kicadSymbolki_keywords': 'memory SRAM', 'kicadSymbolki_description': '1024k x 16 bit low power CMOS SRAM', 'kicadSymbolki_fp_filters': 'TSOP?I*18.4x12mm*P0.5mm*'}])
    newPart['name'].append('Memory_RAM : AS6C1616')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

