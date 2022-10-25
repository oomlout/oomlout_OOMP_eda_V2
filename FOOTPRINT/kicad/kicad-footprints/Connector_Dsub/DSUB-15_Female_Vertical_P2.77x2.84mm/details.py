
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Dsub"
    oIndex = "DSUB-15_Female_Vertical_P2.77x2.84mm"
    hexID = "FZKCNDSUBDSUB15FEMALEVERTICALP277X284"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DSUB-15_Female_Vertical_P2.77x2.84mm', 'description': '15-pin D-Sub connector, straight/vertical, THT-mount, female, pitch 2.77x2.84mm, distance of mounting holes 33.3mm, see https://disti-assets.s3.amazonaws.com/tonar/files/datasheets/16730.pdf', 'tags': '15-pin D-Sub connector straight vertical THT female pitch 2.77x2.84mm mounting holes distance 33.3mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Dsub.3dshapes/DSUB-15_Female_Vertical_P2.77x2.84mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_Dsub : DSUB-15_Female_Vertical_P2.77x2.84mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

