
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Radial_D21.0mm_P19.00mm"
    hexID = "FZKINLRD21P19"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Radial_D21.0mm_P19.00mm', 'description': 'Inductor, Radial series, Radial, pin pitch=19.00mm, , diameter=21mm, http://www.abracon.com/Magnetics/radial/AIRD02.pdf', 'tags': 'Inductor Radial series Radial pin pitch 19.00mm  diameter 21mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_D21.0mm_P19.00mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Radial_D21.0mm_P19.00mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

