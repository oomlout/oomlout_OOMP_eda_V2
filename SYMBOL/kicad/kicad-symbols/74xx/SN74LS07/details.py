
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "SN74LS07"
    hexID = "SZK74XXSN74LS7"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '74LCX07', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SN74LS07', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'www.ti.com/lit/ds/symlink/sn74ls07.pdf', 'kicadSymbolki_keywords': 'TTL hex buffer OpenCol', 'kicadSymbolki_description': 'Hex Buffers and Drivers With Open Collector High Voltage Outputs', 'kicadSymbolki_fp_filters': 'SOIC*3.9x8.7mm*P1.27mm* TSSOP*4.4x5mm*P0.65mm* DIP*W7.62mm*'}])
    newPart['name'].append('74xx : SN74LS07')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

