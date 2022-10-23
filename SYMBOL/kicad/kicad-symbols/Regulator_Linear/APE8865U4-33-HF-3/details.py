
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "APE8865U4-33-HF-3"
    hexID = "SZKREGULATORLINEARAPE8865U433HF3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'APE8865U4-12-HF-3', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'APE8865U4-33-HF-3', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-343_SC-70-4', 'kicadSymbolDatasheet': 'http://www.tme.eu/fr/Document/ced3461ed31ea70a3c416fb648e0cde7/APE8865-3.pdf', 'kicadSymbolki_keywords': '300mA LDO Regulator Fixed Positive', 'kicadSymbolki_description': '300mA Low Dropout Voltage Regulator, Fixed Output 3.3V, SC-70-4', 'kicadSymbolki_fp_filters': '*SC?70*'}])
    newPart['name'].append('APE8865U4-33-HF-3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

