
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "LF256"
    hexID = "SZKAMPLIFIEROPERATIONALLF256"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM741', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LF256', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lf357.pdf', 'kicadSymbolki_keywords': 'single jfet opamp', 'kicadSymbolki_description': 'Single JFET Input Operational Amplifiers, DIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* DIP*W7.62mm* TSSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Amplifier_Operational : LF256')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

