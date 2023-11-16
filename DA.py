#import re
from mp_api.client import MPRester
from pymatgen.io.vasp import Vasprun
from pymatgen.analysis.phase_diagram import PhaseDiagram,PDPlotter
from pymatgen.entries.computed_entries import ComputedStructureEntry
from pymatgen.entries.compatibility import MaterialsProjectCompatibility
#from pymatgen import Element, Composition


vasprun = Vasprun('vasprun.xml')
entry = vasprun.get_computed_entry(inc_structure=True)

#poscar = Poscar.from_file('POSCAR')
#entry = ComputedStructureEntry(poscar.structure, energy)

mpr = MPRester(api_key="XXX")
mp_entries = mpr.get_entries_in_chemsys(['Ba','Co','O'])

compatibility = MaterialsProjectCompatibility()
entry = compatibility.process_entry(entry)
entries = compatibility.process_entries([entry] + mp_entries)

pd = PhaseDiagram(entries) 
# Get the decomposition of your entry
decomposition = pd.get_decomposition(entry.composition)

# Print the structures and fractions in the decomposition
for decomp_entry, fraction in decomposition.items():
	print(f"Materials Project ID:{decomp_entry.entry_id}")
#	print("-".join(decomp_entry.entry_id.split("-")[:2]))
#	data = mpr.get_form_energy_per_atom(str("-".join(decomp_entry.entry_id.split("-")[:2])))
#	print(data)
	print(f"Structure: {decomp_entry.composition.formula}")
	print(f"Energy: {decomp_entry.energy}")
	print(f"Fraction: {fraction}")


 
