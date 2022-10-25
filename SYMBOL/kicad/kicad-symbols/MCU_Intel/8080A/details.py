
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Intel"
    oIndex = "8080A"
    hexID = "SZKMCUINTEL88A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '8080', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '8080A', 'kicadSymbolFootprint': 'Package_DIP:DIP-40_W15.24mm', 'kicadSymbolDatasheet': 'http://datasheets.chipdb.org/Intel/MCS-80/intel-8080.pdf', 'kicadSymbolki_keywords': 'cpu mpu microprocessor', 'kicadSymbolki_description': '8-bit N-channel Microprocessor, DIP-40', 'kicadSymbolki_fp_filters': 'DIP*W15.24*'}])
    newPart['name'].append('MCU_Intel : 8080A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

