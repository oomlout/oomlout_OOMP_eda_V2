
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Heatsink"
    oIndex = "Heatsink_Fischer_FK24413DPAK_23x13mm"
    hexID = "FZKHHFISCHERFK24413DPAK23X13"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Heatsink_Fischer_FK24413DPAK_23x13mm', 'description': '23x13 mm SMD heatsink for TO-252 TO-263 TO-268, https://www.fischerelektronik.de/pim/upload/fischerData/cadpdf/base/fk_244_13_d_pak.pdf', 'tags': 'heatsink TO-252 TO-263 TO-268', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Heatsink.3dshapes/Heatsink_Fischer_FK24413DPAK_23x13mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Heatsink : Heatsink_Fischer_FK24413DPAK_23x13mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

