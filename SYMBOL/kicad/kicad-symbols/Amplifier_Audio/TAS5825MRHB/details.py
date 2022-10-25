
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "TAS5825MRHB"
    hexID = "SZKAMPLIFIERAUDIOTAS5825MRHB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TAS5825MRHB', 'kicadSymbolFootprint': 'Package_DFN_QFN:VQFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm', 'kicadSymbolDatasheet': 'www.ti.com/lit/ds/symlink/tas5825m.pdf', 'kicadSymbolki_keywords': 'Class-D Stereo', 'kicadSymbolki_description': '38-W Stereo, Inductor-Less, Digital Input, Closed-Loop Class-D Audio Amplifier with 192-kHz Extended Audio Processing, VQFN-32', 'kicadSymbolki_fp_filters': 'VQFN*1EP*5x5mm*P0.5mm*'}])
    newPart['name'].append('Amplifier_Audio : TAS5825MRHB')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

