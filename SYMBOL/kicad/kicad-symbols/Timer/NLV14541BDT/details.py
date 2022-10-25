
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer"
    oIndex = "NLV14541BDT"
    hexID = "SZKTIMERNLV14541BDT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CD4541BE', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NLV14541BDT', 'kicadSymbolFootprint': 'Package_SO:TSSOP-14_4.4x5mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pdf/datasheet/mc14541b-d.pdf', 'kicadSymbolki_keywords': 'cmos', 'kicadSymbolki_description': '18V, Programmable Timer, AEC Q100, TSSOP-14', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('Timer : NLV14541BDT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

