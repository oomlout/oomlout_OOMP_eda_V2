
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "FT5HV"
    hexID = "SZKOCSFT5HV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FT5HV', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_Fox_FT5H_5.0x3.2mm', 'kicadSymbolDatasheet': 'https://foxonline.com/wp-content/uploads/pdfs/T5HN_T5HV.pdf', 'kicadSymbolki_keywords': 'TXCO VCTCXO', 'kicadSymbolki_description': 'HCMOS temperature compensated voltage controlled oscillator', 'kicadSymbolki_fp_filters': 'Oscillator*SMD*Fox*FT5H*5.0x3.2mm*'}])
    newPart['name'].append('Oscillator : FT5HV')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

