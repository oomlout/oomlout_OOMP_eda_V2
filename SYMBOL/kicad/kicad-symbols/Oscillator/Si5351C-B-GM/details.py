
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "Si5351C-B-GM"
    hexID = "SZKOCSSI5351CBGM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'Si5351C-B-GM', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-20-1EP_4x4mm_P0.5mm_EP2.7x2.7mm', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/Si5351-B.pdf', 'kicadSymbolki_keywords': 'CMOS Synth Oscillator I2C', 'kicadSymbolki_description': 'I2C Programmable Any-Frequency CMOS Clock Generator, QFN-20', 'kicadSymbolki_fp_filters': 'QFN*1EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('Oscillator : Si5351C-B-GM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

