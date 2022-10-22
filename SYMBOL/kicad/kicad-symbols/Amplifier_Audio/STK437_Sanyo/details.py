
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "STK437_Sanyo"
    hexID = "SZKAMPLIFIERAUDIOSTK437SANYO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STK437_Sanyo', 'kicadSymbolFootprint': 'Package_SIP:Sanyo_STK4xx-15_78.0x8.0mm_P2.54mm', 'kicadSymbolDatasheet': 'http://datasheet.octopart.com/STK430-Sanyo-datasheet-107060.pdf', 'kicadSymbolki_keywords': 'audio amplifier 2ch', 'kicadSymbolki_description': '2-Channel 12 Wmin Audio Frequency Power Amplifier, 4010, SIP-15', 'kicadSymbolki_fp_filters': 'Sanyo*78.0x8.0mm*P2.54mm*'}])
    newPart['name'].append('STK437_Sanyo')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

