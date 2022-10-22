
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "IS31AP4991-GRLS2"
    hexID = "SZKAMPLIFIERAUDIOIS31AP4991GRLS2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IS31AP4991-GRLS2', 'kicadSymbolFootprint': 'Package_SO:SOP-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.issi.com/WW/pdf/31AP4991.pdf', 'kicadSymbolki_keywords': 'ultra low consumption distortion', 'kicadSymbolki_description': '1.2W, 2.7-5.5V, Audio Power Amplifier, Active-Low Standby, SOP-8', 'kicadSymbolki_fp_filters': 'SOP*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('IS31AP4991-GRLS2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

