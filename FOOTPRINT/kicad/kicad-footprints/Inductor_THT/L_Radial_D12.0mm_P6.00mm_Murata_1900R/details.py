
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Radial_D12.0mm_P6.00mm_Murata_1900R"
    hexID = "FZKINLRD12P6M19R"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Radial_D12.0mm_P6.00mm_Murata_1900R', 'description': 'Inductor, Radial series, Radial, pin pitch=6.00mm, , diameter=12.0mm, MuRATA, 1900R, http://www.murata-ps.com/data/magnetics/kmp_1900r.pdf', 'tags': 'Inductor Radial series Radial pin pitch 6.00mm  diameter 12.0mm MuRATA 1900R', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_D12.0mm_P6.00mm_Murata_1900R.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Radial_D12.0mm_P6.00mm_Murata_1900R')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

