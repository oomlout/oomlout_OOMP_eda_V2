
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Radial_D10.5mm_P4.00x5.00mm_Murata_1200RS"
    hexID = "FZKINLRD15P4X5M12RS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Radial_D10.5mm_P4.00x5.00mm_Murata_1200RS', 'description': 'Inductor, Radial, Pitch=4.00x5.00mm, Diameter=10.5mm, Murata 1200RS, http://www.murata-ps.com/data/magnetics/kmp_1200rs.pdf', 'tags': 'Inductor Radial Murata 1200RS', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_D10.5mm_P4.00x5.00mm_Murata_1200RS.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Radial_D10.5mm_P4.00x5.00mm_Murata_1200RS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

