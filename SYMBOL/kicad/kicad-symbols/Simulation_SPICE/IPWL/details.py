
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Simulation_SPICE"
    oIndex = "IPWL"
    hexID = "SZKSIMULATIONSPICEIPWL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'I', 'kicadSymbolValue': 'IPWL', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolSpice_Netlist_Enabled': 'Y', 'kicadSymbolSpice_Primitive': 'I', 'kicadSymbolSpice_Model': 'pwl(0 -1 50n -1 51n 0 97n 1 171n -1 200n -1)', 'kicadSymbolki_keywords': 'simulation', 'kicadSymbolki_description': 'Current source, piece-wise linear'}])
    newPart['name'].append('Simulation_SPICE : IPWL')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

