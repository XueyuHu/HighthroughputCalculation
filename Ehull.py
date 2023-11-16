import pymatgen
from mp_api.client import MPRester
from pymatgen.io.vasp import Vasprun
from pymatgen.analysis.phase_diagram import PhaseDiagram,PDPlotter
from pymatgen.entries.computed_entries import ComputedStructureEntry
from pymatgen.entries.compatibility import MaterialsProjectCompatibility
#
vasprun = Vasprun('vasprun.xml')
entry = vasprun.get_computed_entry(inc_structure=True)
#
mpr = MPRester(api_key='XXX')
mp_entries = mpr.get_entries_in_chemsys(['Ba','Co','O'])
#
compatibility = MaterialsProjectCompatibility()
entry = compatibility.process_entry(entry)
entries = compatibility.process_entries([entry] + mp_entries)
#
pd = PhaseDiagram(entries)
ehull = pd.get_e_above_hull(entry)
print("The energy above hull  is %.3f eV/atom." % ehull)

