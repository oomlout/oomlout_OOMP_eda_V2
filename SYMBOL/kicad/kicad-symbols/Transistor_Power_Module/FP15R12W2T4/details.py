
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_Power_Module"
    oIndex = "FP15R12W2T4"
    hexID = "SZKTRANSISTORPOWERMOFP15R12W2T4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'A2C25S12M3', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FP15R12W2T4', 'kicadSymbolFootprint': 'Transistor_Power_Module:Infineon_EasyPIM-2B', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-FP15R12W2T4-DS-v03_00-en_de.pdf?fileId=db3a30433ba77ced013bae67c3eb3a5e', 'kicadSymbolki_keywords': 'IGBT Power Module Trench Field Stop Technology', 'kicadSymbolki_description': '15A, 1200V, 145W, 3-phase, Freewheeling Diode, Brake Chopper, Diode Rectifier, 5k NTC, EasyPIM-2B', 'kicadSymbolki_fp_filters': 'Infineon*EasyPIM*2B*'}])
    newPart['name'].append('Transistor_Power_Module : FP15R12W2T4')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

