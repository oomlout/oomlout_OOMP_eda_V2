
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Horizontal_D11.2mm_P17.00mm_Diameter12-5mm_Amidon-T44"
    hexID = "FZKINLTOROIDHORIZONTALD112P17DIAMETER125AMIDONT44"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Horizontal_D11.2mm_P17.00mm_Diameter12-5mm_Amidon-T44', 'description': 'L_Toroid, Horizontal series, Radial, pin pitch=17.00mm, , diameter=11.176mm, Diameter12-5mm, Amidon-T44', 'tags': 'L_Toroid Horizontal series Radial pin pitch 17.00mm  diameter 11.176mm Diameter12-5mm Amidon-T44', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Horizontal_D11.2mm_P17.00mm_Diameter12-5mm_Amidon-T44.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Horizontal_D11.2mm_P17.00mm_Diameter12-5mm_Amidon-T44')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

