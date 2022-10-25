
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer"
    oIndex = "TLC555xPS"
    hexID = "SZKTIMERTLC555XPS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM555xMM', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLC555xPS', 'kicadSymbolFootprint': 'Package_SO:VSSOP-8_3.0x3.0mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tlc555.pdf', 'kicadSymbolki_keywords': 'single timer 555', 'kicadSymbolki_description': 'Single LinCMOS Timer, 555 compatible, VSSOP-8', 'kicadSymbolki_fp_filters': '*VSSOP*3.0x3.0mm*P0.65mm*'}])
    newPart['name'].append('Timer : TLC555xPS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

