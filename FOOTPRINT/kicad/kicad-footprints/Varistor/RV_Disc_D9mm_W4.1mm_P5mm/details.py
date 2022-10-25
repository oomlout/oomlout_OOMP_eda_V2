
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Varistor"
    oIndex = "RV_Disc_D9mm_W4.1mm_P5mm"
    hexID = "FZKVRVDISCD9W41P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'RV_Disc_D9mm_W4.1mm_P5mm', 'description': 'Varistor, diameter 9mm, width 4.1mm, pitch 5mm', 'tags': 'varistor SIOV', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Varistor.3dshapes/RV_Disc_D9mm_W4.1mm_P5mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Varistor : RV_Disc_D9mm_W4.1mm_P5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

