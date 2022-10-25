
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LP3982IMM-3.3"
    hexID = "SZKREGULATORLINEARLP3982I33"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LP3982IMM-1.8', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LP3982IMM-3.3', 'kicadSymbolFootprint': 'Package_SO:VSSOP-8_3.0x3.0mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lp3982.pdf', 'kicadSymbolki_keywords': 'linear regulator', 'kicadSymbolki_description': '3.3V, 300mA, Micropower, Ultra-Low-Dropout, Low-Noise CMOS Regulator, VSSOP-8', 'kicadSymbolki_fp_filters': 'VSSOP*3.0x3.0mm*P0.65mm*'}])
    newPart['name'].append('Regulator_Linear : LP3982IMM-3.3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

