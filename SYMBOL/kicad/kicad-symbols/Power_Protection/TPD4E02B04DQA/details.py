
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "TPD4E02B04DQA"
    hexID = "SZKPOWERPROTECTIONTPD4E2B4DQA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPD4E02B04DQA', 'kicadSymbolFootprint': 'Package_SON:USON-10_2.5x1.0mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tpd4e02b04.pdf', 'kicadSymbolki_keywords': 'ESD protection USB HDMI', 'kicadSymbolki_description': '4-Channel ESD Protection Diode for USB Type-C and HDMI 2.0, USON-10', 'kicadSymbolki_fp_filters': 'USON*2.5x1.0mm*P0.5mm*'}])
    newPart['name'].append('TPD4E02B04DQA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

