
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "OPA2376xxYZD"
    hexID = "SZKAMPLIFIEROPERATIONALOPA2376XXYZD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'OPA2376xxYZD', 'kicadSymbolFootprint': 'Package_BGA:Texas_DSBGA-8_0.9x1.9mm_Layout2x4_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/opa376.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'dual opamp', 'kicadSymbolki_description': 'Dual Low-Noise, Low Quiescent Current, Precision Operational Amplifier e-trim Series, DSBGA-8', 'kicadSymbolki_fp_filters': 'Texas*DSBGA*0.9x1.9mm*0.5mm*'}])
    newPart['name'].append('Amplifier_Operational : OPA2376xxYZD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

