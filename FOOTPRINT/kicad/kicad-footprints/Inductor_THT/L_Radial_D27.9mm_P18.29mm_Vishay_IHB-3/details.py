
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Radial_D27.9mm_P18.29mm_Vishay_IHB-3"
    hexID = "FZKINLRD279P1829VISHAYIHB3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Radial_D27.9mm_P18.29mm_Vishay_IHB-3', 'description': 'Inductor, Radial series, Radial, pin pitch=18.29mm, , diameter=27.9mm, Vishay, IHB-3, http://www.vishay.com/docs/34015/ihb.pdf', 'tags': 'Inductor Radial series Radial pin pitch 18.29mm  diameter 27.9mm Vishay IHB-3', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_D27.9mm_P18.29mm_Vishay_IHB-3.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Radial_D27.9mm_P18.29mm_Vishay_IHB-3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

