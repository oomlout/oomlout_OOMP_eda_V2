
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "BTS50055-1TMC"
    hexID = "SZKPOWERMANAGEMENTBTS5551TMC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BTS50055-1TMA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BTS50055-1TMC', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-7_TabPin4', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-BTS50055-1TMC-DS-v01_00-EN.pdf?fileId=5546d4625a888733015aa9b0007235e9', 'kicadSymbolki_keywords': 'BTS50055 PROFET', 'kicadSymbolki_description': 'Smart High-Side Power Switch, PROFET, Single, 6mOhm, 17A, 34V, TO220-7', 'kicadSymbolki_fp_filters': 'TO*263*TabPin4*'}])
    newPart['name'].append('BTS50055-1TMC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

