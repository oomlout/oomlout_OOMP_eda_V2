
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "BTS50010-1TAD"
    hexID = "SZKPOWERMANAGEMENTBTS511TAD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BTS50010-1TAD', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-7_TabPin4', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-BTS50010-1TAD-DS-v01_00-EN.pdf?fileId=5546d462576f34750157c38810ca55cd', 'kicadSymbolki_keywords': 'BTS50010 PROFET', 'kicadSymbolki_description': 'Smart High-Side Power Switch, PROFET, Single, 1mOhm, 40A, 18V, TO-263-7', 'kicadSymbolki_fp_filters': 'TO*263*TabPin4*'}])
    newPart['name'].append('BTS50010-1TAD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

