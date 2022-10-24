
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_SMD"
    oIndex = "Relay_Fujitsu_FTR-B3S"
    hexID = "FZKRELAYSMRELAYFUJITSUFTRB3S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_Fujitsu_FTR-B3S', 'description': 'https://www.fujitsu.com/downloads/MICRO/fcai/relays/ftr-b3.pdf', 'tags': 'Fujitsh FTR B3S B3SA Relay J JLeg', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_SMD.3dshapes/Relay_Fujitsu_FTR-B3S.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Relay_SMD : Relay_Fujitsu_FTR-B3S')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

