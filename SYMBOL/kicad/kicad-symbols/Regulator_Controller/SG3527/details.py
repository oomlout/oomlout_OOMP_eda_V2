
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "SG3527"
    hexID = "SZKREGULATORCONTROLLERSG3527"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SG3525', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SG3527', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.microsemi.com/document-portal/doc_view/11120-sg1525a-sg1527a-datasheet', 'kicadSymbolki_keywords': 'SMPS PWM Controller', 'kicadSymbolki_description': 'Regulating Pulse Width Modulators, OR Logic, PDIP-16/SOIC-16', 'kicadSymbolki_fp_filters': 'SOIC*16*3.9x9.9mm*P1.27mm* SOIC*16*7.5x10.3mm*P1.27mm* DIP*16*W7.62mm*'}])
    newPart['name'].append('SG3527')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

