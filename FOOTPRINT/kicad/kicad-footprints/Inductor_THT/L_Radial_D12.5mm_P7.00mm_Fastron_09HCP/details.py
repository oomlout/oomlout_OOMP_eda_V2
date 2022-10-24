
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Radial_D12.5mm_P7.00mm_Fastron_09HCP"
    hexID = "FZKINLRD125P7FASTRON9HCP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Radial_D12.5mm_P7.00mm_Fastron_09HCP', 'description': 'Inductor, Radial series, Radial, pin pitch=7.00mm, , diameter=12.5mm, Fastron, 09HCP, http://cdn-reichelt.de/documents/datenblatt/B400/DS_09HCP.pdf', 'tags': 'Inductor Radial series Radial pin pitch 7.00mm  diameter 12.5mm Fastron 09HCP', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_D12.5mm_P7.00mm_Fastron_09HCP.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Radial_D12.5mm_P7.00mm_Fastron_09HCP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

