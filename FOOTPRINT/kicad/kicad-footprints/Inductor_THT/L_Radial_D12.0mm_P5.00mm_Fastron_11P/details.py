
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Radial_D12.0mm_P5.00mm_Fastron_11P"
    hexID = "FZKINLRD12P5FASTRON11P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Radial_D12.0mm_P5.00mm_Fastron_11P', 'description': 'Inductor, Radial series, Radial, pin pitch=5.00mm, , diameter=12.0mm, Fastron, 11P, http://cdn-reichelt.de/documents/datenblatt/B400/DS_11P.pdf', 'tags': 'Inductor Radial series Radial pin pitch 5.00mm  diameter 12.0mm Fastron 11P', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_D12.0mm_P5.00mm_Fastron_11P.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Radial_D12.0mm_P5.00mm_Fastron_11P')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

