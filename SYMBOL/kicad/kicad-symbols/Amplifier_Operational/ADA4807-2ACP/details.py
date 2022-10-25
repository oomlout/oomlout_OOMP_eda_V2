
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "ADA4807-2ACP"
    hexID = "SZKAMPLIFIEROPERATIONALADA4872ACP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADA4807-2ACP', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-10-1EP_3x3mm_P0.5mm_EP1.55x2.48mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADA4807-1_4807-2_4807-4.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'dual opamp', 'kicadSymbolki_description': 'Dual Rail-to-Rail Input/Output Amplifiers, with disable, SC-70-6/SOT-23-6', 'kicadSymbolki_fp_filters': 'DFN*3x3mm*P0.5mm*'}])
    newPart['name'].append('Amplifier_Operational : ADA4807-2ACP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

