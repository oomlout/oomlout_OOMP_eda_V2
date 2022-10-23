
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "AAT1217ICA-3.3"
    hexID = "SZKREGULATORSWITCHINGAAT1217ICA33"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AAT1217ICA-1.2', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AAT1217ICA-3.3', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23-6', 'kicadSymbolDatasheet': 'http://www.skyworksinc.com/uploads/documents/AAT1217_202050B.pdf', 'kicadSymbolki_keywords': 'regulator step-up', 'kicadSymbolki_description': '600mA, 3.3V, 1.2MHz, Micropower Synchronous Step-Up Converter, TSOT-23-6', 'kicadSymbolki_fp_filters': 'TSOT?23*'}])
    newPart['name'].append('AAT1217ICA-3.3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

