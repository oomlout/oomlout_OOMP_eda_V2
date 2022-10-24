
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Radial_D9.5mm_P5.00mm_Fastron_07HVP"
    hexID = "FZKINLRD95P5FASTRON7HVP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Radial_D9.5mm_P5.00mm_Fastron_07HVP', 'description': 'Inductor, Radial series, Radial, pin pitch=5.00mm, , diameter=9.5mm, Fastron, 07HVP, http://www.fastrongroup.com/image-show/107/07HVP%2007HVP_T.pdf?type=Complete-DataSheet&productType=series', 'tags': 'Inductor Radial series Radial pin pitch 5.00mm  diameter 9.5mm Fastron 07HVP', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_D9.5mm_P5.00mm_Fastron_07HVP.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Radial_D9.5mm_P5.00mm_Fastron_07HVP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

