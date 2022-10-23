
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Audio"
    oIndex = "Jack_3.5mm_CUI_SJ-3523-SMT_Horizontal"
    hexID = "FZKCNAUDIOJ35CUISJ3523SHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Jack_3.5mm_CUI_SJ-3523-SMT_Horizontal', 'description': '3.5 mm, Stereo, Right Angle, Surface Mount (SMT), Audio Jack Connector (https://www.cui.com/product/resource/sj-352x-smt-series.pdf)', 'tags': '3.5mm audio cui horizontal jack stereo', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_3.5mm_CUI_SJ-3523-SMT_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Audio : Jack_3.5mm_CUI_SJ-3523-SMT_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

