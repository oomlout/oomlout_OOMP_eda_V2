
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "Si5351A-B-GT"
    hexID = "SZKOCSSI5351ABGT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'Si5351A-B-GT', 'kicadSymbolFootprint': 'Package_SO:MSOP-10_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/Si5351-B.pdf', 'kicadSymbolki_keywords': 'CMOS Synth Oscillator I2C', 'kicadSymbolki_description': 'I2C Programmable Any-Frequency CMOS Clock Generator, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Oscillator : Si5351A-B-GT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

