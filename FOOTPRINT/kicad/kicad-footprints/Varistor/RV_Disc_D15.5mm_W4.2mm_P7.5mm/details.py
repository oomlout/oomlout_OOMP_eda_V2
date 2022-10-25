
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Varistor"
    oIndex = "RV_Disc_D15.5mm_W4.2mm_P7.5mm"
    hexID = "FZKVRVDISCD155W42P75"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'RV_Disc_D15.5mm_W4.2mm_P7.5mm', 'description': 'Varistor, diameter 15.5mm, width 4.2mm, pitch 7.5mm', 'tags': 'varistor SIOV', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Varistor.3dshapes/RV_Disc_D15.5mm_W4.2mm_P7.5mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Varistor : RV_Disc_D15.5mm_W4.2mm_P7.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

