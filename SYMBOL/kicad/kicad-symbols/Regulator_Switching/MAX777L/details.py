
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "MAX777L"
    hexID = "SZKREGULATORSWITCHINGMAX777L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX777L', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://kanga.gerbilator.org/ICs/MAX777.pdf', 'kicadSymbolki_keywords': 'switching regulator boost step-up dc-dc', 'kicadSymbolki_description': '210mA, Low voltage input, step-up DC-DC converter, 5V output voltage, DIP-8/SO-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Regulator_Switching : MAX777L')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

