
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "TL071"
    hexID = "SZKAMPLIFIEROPERATIONALTL71"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM741', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TL071', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tl071.pdf', 'kicadSymbolki_keywords': 'singel opamp', 'kicadSymbolki_description': 'Single Low-Noise JFET-Input Operational Amplifiers, DIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* DIP*W7.62mm* TSSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Amplifier_Operational : TL071')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

