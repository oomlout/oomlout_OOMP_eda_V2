
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "OPA1622"
    hexID = "SZKAMPLIFIERAUDIOOPA1622"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'OPA1622', 'kicadSymbolFootprint': 'Package_SON:Texas_S-PVSON-N10', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/opa1622.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'dual opamp audio', 'kicadSymbolki_description': 'High-Fidelity, Bipolar-Input, Audio Operational Amplifier, VSON-10', 'kicadSymbolki_fp_filters': 'Texas*PVSON*'}])
    newPart['name'].append('OPA1622')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

