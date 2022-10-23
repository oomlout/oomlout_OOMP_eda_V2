
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM2735XMF"
    hexID = "SZKREGULATORSWITCHINGLM2735XMF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LMR10510XMF', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2735XMF', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm2735.pdf', 'kicadSymbolki_keywords': 'Miniature Step-Up Boost Flyback SEPIC Voltage Regulator', 'kicadSymbolki_description': 'LM27313, 2.1A, 24Vout Boost/FlybacK/SEPIC Voltage Regulator, 520kHz/1.6MHz Frequency,', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('LM2735XMF')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

