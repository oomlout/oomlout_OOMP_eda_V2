
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "IR4311"
    hexID = "SZKAMPLIFIERAUDIOIR4311"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IR4301', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IR4311', 'kicadSymbolFootprint': 'Package_DFN_QFN:Infineon_PQFN-22-15-4EP_6x5mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/ir4301.pdf?fileId=5546d462533600a4015355d5fc691819', 'kicadSymbolki_keywords': 'integrated class d amplifier', 'kicadSymbolki_description': 'PowIRaudio Integrated Analog Input Class D Audio Amplifier, 90W/4ohm, 60V, PQFN-22', 'kicadSymbolki_fp_filters': 'Infineon*PQFN*4EP*6x5mm*P0.65mm*'}])
    newPart['name'].append('Amplifier_Audio : IR4311')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

