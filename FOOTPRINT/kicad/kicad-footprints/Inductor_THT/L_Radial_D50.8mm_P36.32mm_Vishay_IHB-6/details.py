
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Radial_D50.8mm_P36.32mm_Vishay_IHB-6"
    hexID = "FZKINLRD58P3632VISHAYIHB6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Radial_D50.8mm_P36.32mm_Vishay_IHB-6', 'description': 'Inductor, Radial series, Radial, pin pitch=36.32mm, , diameter=50.8mm, Vishay, IHB-6, http://www.vishay.com/docs/34015/ihb.pdf', 'tags': 'Inductor Radial series Radial pin pitch 36.32mm  diameter 50.8mm Vishay IHB-6', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_D50.8mm_P36.32mm_Vishay_IHB-6.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Radial_D50.8mm_P36.32mm_Vishay_IHB-6')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

