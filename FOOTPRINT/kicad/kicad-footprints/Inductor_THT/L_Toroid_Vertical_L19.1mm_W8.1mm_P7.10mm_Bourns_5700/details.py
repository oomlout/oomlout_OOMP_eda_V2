
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Vertical_L19.1mm_W8.1mm_P7.10mm_Bourns_5700"
    hexID = "FZKINLTOROIDVERTICALL191W81P71BOURNS57"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Vertical_L19.1mm_W8.1mm_P7.10mm_Bourns_5700', 'description': 'L_Toroid, Vertical series, Radial, pin pitch=7.10mm, , length*width=19.1*8.1mm^2, Bourns, 5700, http://www.bourns.com/docs/Product-Datasheets/5700_series.pdf', 'tags': 'L_Toroid Vertical series Radial pin pitch 7.10mm  length 19.1mm width 8.1mm Bourns 5700', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Vertical_L19.1mm_W8.1mm_P7.10mm_Bourns_5700.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Vertical_L19.1mm_W8.1mm_P7.10mm_Bourns_5700')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

