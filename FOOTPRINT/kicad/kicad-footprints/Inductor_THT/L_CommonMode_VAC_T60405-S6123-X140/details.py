
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_CommonMode_VAC_T60405-S6123-X140"
    hexID = "FZKINLCOONMODEVACT645S6123X14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_CommonMode_VAC_T60405-S6123-X140', 'description': '3 Phase, CM Choke, https://vacuumschmelze.com/03_Documents/Datasheets%20-%20Drawings/Commom-Mode-Chokes/6123-X140.pdf', 'tags': 'common mode filter', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_CommonMode_VAC_T60405-S6123-X140.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_CommonMode_VAC_T60405-S6123-X140')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

