
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Dsub"
    oIndex = "DSUB-25_Male_Vertical_P2.77x2.84mm"
    hexID = "FZKCNDSUBDSUB25MALEVERTICALP277X284"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DSUB-25_Male_Vertical_P2.77x2.84mm', 'description': '25-pin D-Sub connector, straight/vertical, THT-mount, male, pitch 2.77x2.84mm, distance of mounting holes 47.1mm, see https://disti-assets.s3.amazonaws.com/tonar/files/datasheets/16730.pdf', 'tags': '25-pin D-Sub connector straight vertical THT male pitch 2.77x2.84mm mounting holes distance 47.1mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Dsub.3dshapes/DSUB-25_Male_Vertical_P2.77x2.84mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_Dsub : DSUB-25_Male_Vertical_P2.77x2.84mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

