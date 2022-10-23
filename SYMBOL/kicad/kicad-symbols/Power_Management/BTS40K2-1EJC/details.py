
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "BTS40K2-1EJC"
    hexID = "SZKPOWERMANAGEMENTBTS4K21EJC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BTS40K2-1EJC', 'kicadSymbolFootprint': 'Package_SO:Infineon_PG-DSO-8-43', 'kicadSymbolDatasheet': 'http://www.infineon.com/dgdl/Infineon-BTS40K2-1EJC-DS-v01_00-EN.pdf?fileId=5546d462518ffd85015254ee4e601f99', 'kicadSymbolki_keywords': 'infineon power switch', 'kicadSymbolki_description': 'Smart High-Side Power Switch, PROFET, Single, 200mOhm, 1.5A, 36V, DSO-8', 'kicadSymbolki_fp_filters': 'Infineon*PG*DSO*43*'}])
    newPart['name'].append('BTS40K2-1EJC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

