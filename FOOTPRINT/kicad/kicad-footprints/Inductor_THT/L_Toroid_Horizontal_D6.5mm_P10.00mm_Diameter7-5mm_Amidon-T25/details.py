
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Horizontal_D6.5mm_P10.00mm_Diameter7-5mm_Amidon-T25"
    hexID = "FZKINLTOROIDHORIZONTALD65P1DIAMETER75AMIDONT25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Horizontal_D6.5mm_P10.00mm_Diameter7-5mm_Amidon-T25', 'description': 'L_Toroid, Horizontal series, Radial, pin pitch=10.00mm, , diameter=6.476999999999999mm, Diameter7-5mm, Amidon-T25', 'tags': 'L_Toroid Horizontal series Radial pin pitch 10.00mm  diameter 6.476999999999999mm Diameter7-5mm Amidon-T25', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Horizontal_D6.5mm_P10.00mm_Diameter7-5mm_Amidon-T25.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Horizontal_D6.5mm_P10.00mm_Diameter7-5mm_Amidon-T25')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

