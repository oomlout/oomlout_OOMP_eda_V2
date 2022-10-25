
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Horizontal_D32.5mm_P28.90mm_Bourns_2300"
    hexID = "FZKINLTOROIDHORIZONTALD325P289BOURNS23"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Horizontal_D32.5mm_P28.90mm_Bourns_2300', 'description': 'L_Toroid, Horizontal series, Radial, pin pitch=28.90mm, , diameter=32.5mm, Bourns, 2300, http://www.bourns.com/docs/Product-Datasheets/2300_series.pdf?sfvrsn=3', 'tags': 'L_Toroid Horizontal series Radial pin pitch 28.90mm  diameter 32.5mm Bourns 2300', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Horizontal_D32.5mm_P28.90mm_Bourns_2300.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Horizontal_D32.5mm_P28.90mm_Bourns_2300')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

