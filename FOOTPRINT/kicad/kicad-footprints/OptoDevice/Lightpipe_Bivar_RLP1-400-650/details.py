
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "Lightpipe_Bivar_RLP1-400-650"
    hexID = "FZKOPLIGHTPIPEBIVARRLP1465"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Lightpipe_Bivar_RLP1-400-650', 'description': '1-way, 2.8mm lightpipe, 10mm lens output height, 17mm protrusion, https://www.bivar.com/parts_content/Datasheets/RLP1-XXX-XXX.pdf', 'tags': 'planar light pipe 1 way 3mm ', 'attributeType': None, 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Lightpipe_Bivar_RLP1-400-650.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'oval'}})
    newPart['name'].append('OptoDevice : Lightpipe_Bivar_RLP1-400-650')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

