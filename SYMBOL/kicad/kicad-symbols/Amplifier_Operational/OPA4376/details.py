
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "OPA4376"
    hexID = "SZKAMPLIFIEROPERATIONALOPA4376"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM2902', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'OPA4376', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/opa376.pdf', 'kicadSymbolki_keywords': 'quad opamp', 'kicadSymbolki_description': 'Quad Low-Noise, Low Quiescent Current, Precision Operational Amplifier e-trim Series, SC-70-5', 'kicadSymbolki_fp_filters': 'SOIC*3.9x8.7mm*P1.27mm* DIP*W7.62mm* TSSOP*4.4x5mm*P0.65mm* SSOP*5.3x6.2mm*P0.65mm* MSOP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Amplifier_Operational : OPA4376')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

