
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Dsub"
    oIndex = "DSUB-9_Male_Vertical_P2.77x2.84mm"
    hexID = "FZKCNDSUBDSUB9MALEVERTICALP277X284"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DSUB-9_Male_Vertical_P2.77x2.84mm', 'description': '9-pin D-Sub connector, straight/vertical, THT-mount, male, pitch 2.77x2.84mm, distance of mounting holes 25mm, see https://disti-assets.s3.amazonaws.com/tonar/files/datasheets/16730.pdf', 'tags': '9-pin D-Sub connector straight vertical THT male pitch 2.77x2.84mm mounting holes distance 25mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Dsub.3dshapes/DSUB-9_Male_Vertical_P2.77x2.84mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_Dsub : DSUB-9_Male_Vertical_P2.77x2.84mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

