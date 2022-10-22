
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "IR4302"
    hexID = "SZKAMPLIFIERAUDIOIR432"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IR4302', 'kicadSymbolFootprint': 'Package_DFN_QFN:Infineon_PQFN-44-31-5EP_7x7mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/ir4302.pdf?fileId=5546d462533600a4015355d602a9181d', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'integrated class d amplifier 2ch', 'kicadSymbolki_description': 'PowIRaudio 2 Channel Integrated Analog Input Class D Audio Amplifier, 130W/4ohm, 80V, PQFN-44', 'kicadSymbolki_fp_filters': 'Infineon*PQFN*5EP*7x7mm*P0.5mm*'}])
    newPart['name'].append('IR4302')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

