
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "BTS716GB"
    hexID = "SZKPOWERMANAGEMENTBTS716GB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BTS724G', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BTS716GB', 'kicadSymbolFootprint': 'Package_SO:Infineon_PG-DSO-20-32', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-BTS716GB-DS-v01_00-EN.pdf?fileId=5546d4625a888733015aa3be94e21008', 'kicadSymbolki_keywords': 'High_Side_Switch Power', 'kicadSymbolki_description': 'Smart High-Side Power Switch, PROFET, 4 Channel, 140mOhm, 2.6A, 40V, DSO-20', 'kicadSymbolki_fp_filters': 'Infineon*PG*DSO*'}])
    newPart['name'].append('BTS716GB')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

