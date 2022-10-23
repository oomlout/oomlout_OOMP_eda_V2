
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "PAM2306AYPBB"
    hexID = "SZKREGULATORSWITCHINGPAM236AYPBB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PAM2306AYPAA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PAM2306AYPBB', 'kicadSymbolFootprint': 'Package_DFN_QFN:WDFN-12-1EP_3x3mm_P0.45mm_EP1.7x2.5mm', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/PAM2306.pdf', 'kicadSymbolki_keywords': 'STEP-DOWN Dual channel 1A Out1 1.2V, Out2 1.2V', 'kicadSymbolki_description': '1A, Dual Step-Down DC/DC-Converter, Out1 1.2V, Out2 1.2V, 1.5MHz, W-DFN3x3', 'kicadSymbolki_fp_filters': 'WDFN*3x3mm?P0.45mm*'}])
    newPart['name'].append('PAM2306AYPBB')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

