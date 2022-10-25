
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "BTS6133D"
    hexID = "SZKPOWERMANAGEMENTBTS6133D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BTS50080-1TEA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BTS6133D', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-4', 'kicadSymbolDatasheet': 'http://www.infineon.com/dgdl/Infineon-BTS6133D-DS-v01_00-EN.pdf?fileId=5546d4625a888733015aa3e3286f102a', 'kicadSymbolki_keywords': 'infineon power switch', 'kicadSymbolki_description': 'Smart High-Side Power Switch, PROFET, Single, 10mOhm, 8A, 38V, TO-252-5', 'kicadSymbolki_fp_filters': 'TO*252*'}])
    newPart['name'].append('Power_Management : BTS6133D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

