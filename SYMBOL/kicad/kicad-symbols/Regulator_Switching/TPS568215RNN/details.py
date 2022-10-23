
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS568215RNN"
    hexID = "SZKREGULATORSWITCHINGTPS568215RNN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS568215RNN', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_RNN0018A', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps568215.pdf', 'kicadSymbolki_keywords': 'switching buck converter step-down', 'kicadSymbolki_description': '4.5V-17V Input, 8A Synchronous Step-Down SWIFT Converter, Adjustable Output, 400kHz/800kHz/1.2MHz Switching Frequency, Texas VQFN-18', 'kicadSymbolki_fp_filters': 'Texas*RNN0018A*'}])
    newPart['name'].append('TPS568215RNN')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

