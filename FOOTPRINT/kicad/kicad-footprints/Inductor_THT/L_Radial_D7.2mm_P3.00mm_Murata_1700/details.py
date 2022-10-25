
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Radial_D7.2mm_P3.00mm_Murata_1700"
    hexID = "FZKINLRD72P3M17"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Radial_D7.2mm_P3.00mm_Murata_1700', 'description': 'Inductor, Radial series, Radial, pin pitch=3.00mm, , diameter=7.2mm, MuRATA, 1700, http://www.murata-ps.com/data/magnetics/kmp_1700.pdf', 'tags': 'Inductor Radial series Radial pin pitch 3.00mm  diameter 7.2mm MuRATA 1700', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_D7.2mm_P3.00mm_Murata_1700.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Radial_D7.2mm_P3.00mm_Murata_1700')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

