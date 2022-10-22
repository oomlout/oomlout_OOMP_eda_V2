
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "RD5107A"
    hexID = "SZKAUDIORD517A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'RD5106A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'RD5107A', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://pdf.datasheetarchive.com/indexerfiles/Scans-091/DSAHI00048836.pdf', 'kicadSymbolki_keywords': 'EG&G RETICON BBD N-channel silicon-gate', 'kicadSymbolki_description': 'Analog Delay Line 512 sample bucket brigade device, 1msec to more than 2seconds, input signal frequency range 0 to 170KHz, clock frequency range 500Hz to 1MHz', 'kicadSymbolki_fp_filters': 'DIP-8*'}])
    newPart['name'].append('RD5107A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

