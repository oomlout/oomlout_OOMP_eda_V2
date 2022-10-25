
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "IRS2052M"
    hexID = "SZKAMPLIFIERAUDIOIRS252M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IRS2052M', 'kicadSymbolFootprint': 'Package_DFN_QFN:Infineon_MLPQ-48-1EP_7x7mm_P0.5mm_EP5.55x5.55mm', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irs2052mpbf.pdf?fileId=5546d462533600a401535675d3b32788', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'Gate Driver Class D 2ch', 'kicadSymbolki_description': '2 CH Digital Audio Amplifier, PWM Modulator, +/-100V, 0.5/0.6A, MLPQ-48', 'kicadSymbolki_fp_filters': 'Infineon*MLPQ*1EP*7x7mm*P0.5mm*'}])
    newPart['name'].append('Amplifier_Audio : IRS2052M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

