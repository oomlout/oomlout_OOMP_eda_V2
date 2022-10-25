
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Horizontal_D28.0mm_P26.67mm_Bourns_2200"
    hexID = "FZKINLTOROIDHORIZONTALD28P2667BOURNS22"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Horizontal_D28.0mm_P26.67mm_Bourns_2200', 'description': 'L_Toroid, Horizontal series, Radial, pin pitch=26.67mm, , diameter=28mm, Bourns, 2200, http://www.bourns.com/docs/Product-Datasheets/2100_series.pdf?sfvrsn=3', 'tags': 'L_Toroid Horizontal series Radial pin pitch 26.67mm  diameter 28mm Bourns 2200', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Horizontal_D28.0mm_P26.67mm_Bourns_2200.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Horizontal_D28.0mm_P26.67mm_Bourns_2200')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

