
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Dsub"
    oIndex = "DSUB-37_Male_Horizontal_P2.77x2.54mm_EdgePinOffset9.40mm"
    hexID = "FZKCNDSUBDSUB37MALEHORIZONTALP277X254EDGEPINOFFSET94"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DSUB-37_Male_Horizontal_P2.77x2.54mm_EdgePinOffset9.40mm', 'description': '37-pin D-Sub connector, horizontal/angled (90 deg), THT-mount, male, pitch 2.77x2.54mm, pin-PCB-offset 9.4mm, see http://docs-europe.electrocomponents.com/webdocs/1585/0900766b81585df2.pdf', 'tags': '37-pin D-Sub connector horizontal angled 90deg THT male pitch 2.77x2.54mm pin-PCB-offset 9.4mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Dsub.3dshapes/DSUB-37_Male_Horizontal_P2.77x2.54mm_EdgePinOffset9.40mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_Dsub : DSUB-37_Male_Horizontal_P2.77x2.54mm_EdgePinOffset9.40mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

