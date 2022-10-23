
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "EE2-5TNU"
    hexID = "SZKRELAYEE25TNU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'EE2-3TNU', 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'EE2-5TNU', 'kicadSymbolFootprint': 'Relay_SMD:Relay_DPDT_Kemet_EE2_NU_DoubleCoil', 'kicadSymbolDatasheet': 'https://content.kemet.com/datasheets/KEM_R7002_EC2_EE2.pdf', 'kicadSymbolki_keywords': 'signal relay double pole double throw DPDT DC coil double dual coil latching', 'kicadSymbolki_description': 'General purpose signal relay, Kemet EE2 Series, DPDT (2 Form C), double coil latching, SMD, 60W/125VA, 220VDC/250VAC, 2A, 5V DC coil', 'kicadSymbolki_fp_filters': 'Relay*DPDT*Kemet*EE2*NU*DoubleCoil*'}])
    newPart['name'].append('EE2-5TNU')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

