
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "BTS724G"
    hexID = "SZKPOWERMANAGEMENTBTS724G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BTS724G', 'kicadSymbolFootprint': 'Package_SO:Infineon_PG-DSO-20-32', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-BTS724G-DS-v01_00-EN.pdf?fileId=5546d4625a888733015aa3a2f1030ff1', 'kicadSymbolki_keywords': 'High_Side_Switch Power', 'kicadSymbolki_description': 'Smart High-Side Power Switch, PROFET, 4 Channel, 90mOhm, 3.3A, 40V, DSO-20', 'kicadSymbolki_fp_filters': 'Infineon*PG*DSO*'}])
    newPart['name'].append('Power_Management : BTS724G')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

