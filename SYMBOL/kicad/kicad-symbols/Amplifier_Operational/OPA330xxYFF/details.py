
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "OPA330xxYFF"
    hexID = "SZKAMPLIFIEROPERATIONALOPA33XXYFF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'OPA330xxYFF', 'kicadSymbolFootprint': 'Package_BGA:Texas_DSBGA-5_0.822x1.116mm_Layout2x1x2_P0.4mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/opa330.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': '50μV V OS, 0.25μV/°C, 35μA CMOS OPERATIONAL AMPLIFIERS, Zerø-Drift Series, DSBGA', 'kicadSymbolki_fp_filters': 'Texas*DSBGA*0.822x1.116mm*2x1x2*P0.4mm*'}])
    newPart['name'].append('Amplifier_Operational : OPA330xxYFF')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

