
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "Bus_M.2_Socket_E"
    hexID = "SZKCNBUSM2SOE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Bus_M.2_Socket_E', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://read.pudn.com/downloads794/doc/project/3133918/PCIe_M.2_Electromechanical_Spec_Rev1.0_Final_11012013_RS_Clean.pdf#page=150', 'kicadSymbolki_keywords': 'M2 NGNF PCI-E', 'kicadSymbolki_description': 'M.2 Socket 1-SD Mechanical Key E', 'kicadSymbolki_fp_filters': '*M*2*E*'}])
    newPart['name'].append('Bus_M.2_Socket_E')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

