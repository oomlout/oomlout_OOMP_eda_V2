
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transformer_THT"
    oIndex = "Transformer_CHK_UI30-4VA_Flat"
    hexID = "FZKTRTRCHKUI34VAFLAT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Transformer_CHK_UI30-4VA_Flat', 'description': 'Trafo, Flattrafo, CHK, UI30, 4VA,', 'tags': 'Trafo Flattrafo CHK UI30 4VA ', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transformer_THT.3dshapes/Transformer_CHK_UI30-4VA_Flat.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Transformer_THT : Transformer_CHK_UI30-4VA_Flat')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

