
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Axial_L7.0mm_D3.3mm_P12.70mm_Horizontal_Fastron_MICC"
    hexID = "FZKINLAXIALL7D33P127HORIZONTALFASTRONMICC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Axial_L7.0mm_D3.3mm_P12.70mm_Horizontal_Fastron_MICC', 'description': 'Inductor, Axial series, Axial, Horizontal, pin pitch=12.7mm, , length*diameter=7*3.3mm^2, Fastron, MICC, http://www.fastrongroup.com/image-show/70/MICC.pdf?type=Complete-DataSheet&productType=series', 'tags': 'Inductor Axial series Axial Horizontal pin pitch 12.7mm  length 7mm diameter 3.3mm Fastron MICC', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Axial_L7.0mm_D3.3mm_P12.70mm_Horizontal_Fastron_MICC.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Axial_L7.0mm_D3.3mm_P12.70mm_Horizontal_Fastron_MICC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

