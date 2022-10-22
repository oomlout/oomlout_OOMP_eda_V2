
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "DSP_Freescale"
    oIndex = "DSP96002"
    hexID = "SZKDSPFREESCALEDSP962"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DSP96002', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://cache.freescale.com/files/dsp/doc/inactive/DSP96002.pdf', 'kicadSymbolki_keywords': 'DSP 32bit Dual Port Processor', 'kicadSymbolki_description': '32-bit General Purpose Floating-point DSP, Dual Port, PGA-223', 'kicadSymbolki_fp_filters': 'PGA-223*'}])
    newPart['name'].append('DSP96002')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

