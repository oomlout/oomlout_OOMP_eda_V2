
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "ADA4898-2"
    hexID = "SZKAMPLIFIEROPERATIONALADA48982"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADA4898-2', 'kicadSymbolFootprint': 'Package_SO:SOIC-8-1EP_3.9x4.9mm_P1.27mm_EP2.41x3.81mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ada4898-1_4898-2.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'opamp dual low noise low distortion', 'kicadSymbolki_description': 'Dual High Voltage, Low Noise, Low Distortion, Unity-Gain Stable, High Speed Op Amp, SOIC-8-1EP', 'kicadSymbolki_fp_filters': 'SOIC*1EP*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Amplifier_Operational : ADA4898-2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

