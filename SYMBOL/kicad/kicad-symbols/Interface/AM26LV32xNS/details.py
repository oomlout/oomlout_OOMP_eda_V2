
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "AM26LV32xNS"
    hexID = "SZKINTERFACEAM26LV32XNS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AM26LV32xNS', 'kicadSymbolFootprint': 'Package_SO:SOIC-16W_5.3x10.2mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/am26lv32.pdf', 'kicadSymbolki_keywords': 'receiver rs485 rs422 differential', 'kicadSymbolki_description': '32Mbps 3.3V RS485 Quad Line Receivers, SO-16', 'kicadSymbolki_fp_filters': 'SOIC*5.3x10.2mm*P1.27mm*'}])
    newPart['name'].append('Interface : AM26LV32xNS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

