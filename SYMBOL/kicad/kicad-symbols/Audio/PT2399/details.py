
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "PT2399"
    hexID = "SZKAUDIOPT2399"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PT2399', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://sound.westhost.com/pt2399.pdf', 'kicadSymbolki_keywords': 'CMOS ADC DAC 44K Digital processing VCO', 'kicadSymbolki_description': 'Echo Processor IC', 'kicadSymbolki_fp_filters': 'DIP-16*'}])
    newPart['name'].append('Audio : PT2399')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

