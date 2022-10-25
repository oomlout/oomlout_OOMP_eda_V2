
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "OPA2333xxDRB"
    hexID = "SZKAMPLIFIEROPERATIONALOPA2333XXDRB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'OPA2333xxDRB', 'kicadSymbolFootprint': 'Package_SON:Texas_S-PVSON-N8', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/opa333.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'dual opamp', 'kicadSymbolki_description': 'Dual 1.8V, microPower, CMOS Operational Amplifiers, Zero-Drift Series, SON-8', 'kicadSymbolki_fp_filters': 'Texas*PVSON*'}])
    newPart['name'].append('Amplifier_Operational : OPA2333xxDRB')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

