
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_Power_Module"
    oIndex = "FS75R07N2E4"
    hexID = "SZKTRANSISTORPOWERMOFS75R7N2E4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FS75R07N2E4', 'kicadSymbolFootprint': 'Transistor_Power_Module:Infineon_AG-ECONO2', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-FS75R07N2E4-DS-v02_00-en_de.pdf?fileId=db3a30432f5008fe012f52f916333979', 'kicadSymbolki_keywords': 'IGBT Power Module Trench Field Stop Technology', 'kicadSymbolki_description': '75A, 650V, 250W , 3-phase, Freewheeling Diode, 5k NTC, AG-Econo2', 'kicadSymbolki_fp_filters': '*Infineon*AG*ECONO2*'}])
    newPart['name'].append('FS75R07N2E4')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

