
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "PAM2306DYPAA"
    hexID = "SZKREGULATORSWITCHINGPAM236DYPAA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PAM2306AYPAA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PAM2306DYPAA', 'kicadSymbolFootprint': 'Package_DFN_QFN:WDFN-12-1EP_3x3mm_P0.45mm_EP1.7x2.5mm', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/PAM2306D.pdf', 'kicadSymbolki_keywords': 'STEP-DOWN Dual channel 1A Out1 ADJ, Out2 ADJ', 'kicadSymbolki_description': '1A, Dual Step-Down DC/DC-Converter, Out1 ADJ, Out2 ADJ, 1.5MHz, W-DFN3x3', 'kicadSymbolki_fp_filters': 'WDFN*3x3mm?P0.45mm*'}])
    newPart['name'].append('Regulator_Switching : PAM2306DYPAA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

