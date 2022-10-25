
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "LTC6362xDD"
    hexID = "SZKAMPLIFIEROPERATIONALLTC6362XDD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC6362xDD', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_3x3mm_P0.5mm_EP1.66x2.38mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/6362fa.pdf', 'kicadSymbolki_keywords': 'single differential opamp', 'kicadSymbolki_description': 'Precision, Low Power, Rail-to-Rail Input/Output, Differential Op Amp/SAR ADC Driver, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Amplifier_Operational : LTC6362xDD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

