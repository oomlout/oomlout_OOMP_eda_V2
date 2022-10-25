
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Radial_D29.8mm_P28.80mm_Murata_1400series"
    hexID = "FZKINLRD298P288M14SERIES"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Radial_D29.8mm_P28.80mm_Murata_1400series', 'description': 'Inductor, Radial series, Radial, pin pitch=28.80mm, , diameter=29.8mm, muRATA, 1400series, http://www.murata-ps.com/data/magnetics/kmp_1400.pdf', 'tags': 'Inductor Radial series Radial pin pitch 28.80mm  diameter 29.8mm muRATA 1400series', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_D29.8mm_P28.80mm_Murata_1400series.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Radial_D29.8mm_P28.80mm_Murata_1400series')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

