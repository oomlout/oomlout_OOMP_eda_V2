
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Radial_D7.8mm_P5.00mm_Fastron_07HCP"
    hexID = "FZKINLRD78P5FASTRON7HCP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Radial_D7.8mm_P5.00mm_Fastron_07HCP', 'description': 'Inductor, Radial series, Radial, pin pitch=5.00mm, , diameter=7.8mm, Fastron, 07HCP, http://www.abracon.com/Magnetics/radial/AISR875.pdf', 'tags': 'Inductor Radial series Radial pin pitch 5.00mm  diameter 7.8mm Fastron 07HCP', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_D7.8mm_P5.00mm_Fastron_07HCP.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Radial_D7.8mm_P5.00mm_Fastron_07HCP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

