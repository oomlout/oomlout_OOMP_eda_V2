
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IGOT60R070D1"
    hexID = "SZKTRANSISTORFETIGOT6R7D1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IGOT60R070D1', 'kicadSymbolFootprint': 'Package_SO:Infineon_PG-DSO-20-87', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IGOT60R070D1-DataSheet-v02_11-EN.pdf?fileId=5546d46265f064ff016685fa65066523', 'kicadSymbolki_keywords': 'N-Channel GaN MOSFET', 'kicadSymbolki_description': '31A Id, 600V Vds, 70mOhm, N-Channel GaN MOSFET, PD-DSO-20-87', 'kicadSymbolki_fp_filters': 'Infineon*PG*DSO*87*'}])
    newPart['name'].append('IGOT60R070D1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

