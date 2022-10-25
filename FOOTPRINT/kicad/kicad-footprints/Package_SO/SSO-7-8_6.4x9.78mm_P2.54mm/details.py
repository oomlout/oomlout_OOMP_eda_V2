
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SSO-7-8_6.4x9.78mm_P2.54mm"
    hexID = "FZKSOSSO7864X978P254"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SSO-7-8_6.4x9.78mm_P2.54mm', 'description': 'SSO, 7 Pin (https://b2b-api.panasonic.eu/file_stream/pids/fileversion/2787), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'SSO SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SSO-7-8_6.4x9.78mm_P2.54mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : SSO-7-8_6.4x9.78mm_P2.54mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

