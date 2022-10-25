
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Dsub"
    oIndex = "DSUB-37_Female_Vertical_P2.77x2.84mm"
    hexID = "FZKCNDSUBDSUB37FEMALEVERTICALP277X284"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DSUB-37_Female_Vertical_P2.77x2.84mm', 'description': '37-pin D-Sub connector, straight/vertical, THT-mount, female, pitch 2.77x2.84mm, distance of mounting holes 63.5mm, see https://disti-assets.s3.amazonaws.com/tonar/files/datasheets/16730.pdf', 'tags': '37-pin D-Sub connector straight vertical THT female pitch 2.77x2.84mm mounting holes distance 63.5mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Dsub.3dshapes/DSUB-37_Female_Vertical_P2.77x2.84mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_Dsub : DSUB-37_Female_Vertical_P2.77x2.84mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

