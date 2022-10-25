
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Fuse"
    oIndex = "Fuse_Bourns_TBU-CA"
    hexID = "FZKFUFUBOURNSTBUCA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fuse_Bourns_TBU-CA', 'description': 'Bourns TBU-CA Fuse, 2 Pin (https://www.bourns.com/data/global/pdfs/TBU-CA.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'Bourns Fuse NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuse_Bourns_TBU-CA.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Fuse : Fuse_Bourns_TBU-CA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

