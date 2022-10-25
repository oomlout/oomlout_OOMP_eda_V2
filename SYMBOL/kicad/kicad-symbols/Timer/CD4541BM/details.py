
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer"
    oIndex = "CD4541BM"
    hexID = "SZKTIMERCD4541BM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CD4541BE', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CD4541BM', 'kicadSymbolFootprint': 'Package_SO:SOIC-14_3.9x8.7mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/cd4541b.pdf', 'kicadSymbolki_keywords': 'cmos', 'kicadSymbolki_description': '20V, Programmable Timer, SOIC-14', 'kicadSymbolki_fp_filters': 'SOIC*3.9x8.7mm*P1.27mm*'}])
    newPart['name'].append('Timer : CD4541BM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

