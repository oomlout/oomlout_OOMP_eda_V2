
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_SMD"
    oIndex = "SW_SPST_SKQG_WithoutStem"
    hexID = "FZKBSWITCHSMSWSPSTSKQGWITHOUTSTEM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_SPST_SKQG_WithoutStem', 'description': 'ALPS 5.2mm Square Low-profile Type (Surface Mount) SKQG Series, Without stem, http://www.alps.com/prod/info/E/HTML/Tact/SurfaceMount/SKQG/SKQGAEE010.html', 'tags': 'SPST Button Switch', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_SMD.3dshapes/SW_SPST_SKQG_WithoutStem.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Button_Switch_SMD : SW_SPST_SKQG_WithoutStem')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

