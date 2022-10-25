
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "RD5106A"
    hexID = "SZKAUDIORD516A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'RD5106A', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://pdf.datasheetarchive.com/indexerfiles/Scans-091/DSAHI00048836.pdf', 'kicadSymbolki_keywords': 'EG&G RETICON BBD N-channel silicon-gate', 'kicadSymbolki_description': 'Analog Delay Line 256 sample bucket brigade device, 512usec to more than 1second, input signal frequency range 0 to 170KHz, clock frequency range 500Hz to 1MHz', 'kicadSymbolki_fp_filters': 'DIP-8*'}])
    newPart['name'].append('Audio : RD5106A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

