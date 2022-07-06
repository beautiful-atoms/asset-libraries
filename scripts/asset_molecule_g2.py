from ase.build import molecule
from ase.collections import g2
from batoms import Batoms
from batoms.asset.asset import find_baotms_catalog_uuid, create_asset, push_asset
import bpy
from time import time
from batoms.logger import set_logger, root_logger
import logging
root_logger.setLevel('WARNING')


catalog_id = find_baotms_catalog_uuid('Molecule')
print(catalog_id)
print("Number of molecules: {}".format(len(g2.names)))
i = 0
assets = set()
for name in g2.names:
    # print(name)
    print("="*80)
    bpy.ops.batoms.delete()
    tstart = time()
    atoms = molecule(name)
    batoms = Batoms(label = name, from_ase = atoms)
    metadata = {"author": "Batoms",
                "description": "The G2-database of common molecules.",
                "catalog_id": catalog_id,
                "tags": ["molecule", "g2"]
            }
    asset = create_asset(batoms, model_style = 1, metadata = metadata)
    push_asset('Batoms', 'Molecule.blend', {asset})
    # assets.add(asset)
    print("{}, time: {:1.2f}, {} ".format(i, time() - tstart, name))
    print("="*80)
    i += 1

