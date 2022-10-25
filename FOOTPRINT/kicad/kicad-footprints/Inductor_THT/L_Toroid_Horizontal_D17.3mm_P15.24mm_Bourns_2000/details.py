
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Horizontal_D17.3mm_P15.24mm_Bourns_2000"
    hexID = "FZKINLTOROIDHORIZONTALD173P1524BOURNS2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Horizontal_D17.3mm_P15.24mm_Bourns_2000', 'description': 'L_Toroid, Horizontal series, Radial, pin pitch=15.24mm, , diameter=17.3mm, Bourns, 2000, http://www.bourns.com/docs/Product-Datasheets/2000_series.pdf?sfvrsn=5', 'tags': 'L_Toroid Horizontal series Radial pin pitch 15.24mm  diameter 17.3mm Bourns 2000', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Horizontal_D17.3mm_P15.24mm_Bourns_2000.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Horizontal_D17.3mm_P15.24mm_Bourns_2000')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

