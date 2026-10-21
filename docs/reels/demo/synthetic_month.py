# Synthetic month of outpatient + inpatient visits for the W5 demo. No real data; fixed seed so the numbers repeat.
import csv, random, sys, pathlib
random.seed(20261123)
out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
patients, encounters, dx = [], [], []
enc_id = 0
for p in range(1, 413):                       # 412 synthetic patients seen in the month
    pid = f"P{p:04d}"; patients.append(pid)
    n_visits = 1 + (random.random() < 0.20) + (random.random() < 0.06)   # some come back once, a few twice
    for v in range(n_visits):
        enc_id += 1; eid = f"E{enc_id:05d}"
        encounters.append((eid, pid, f"2026-10-{random.randint(1, 31):02d}"))
        for d in range(random.choice([1, 1, 2, 2, 3])):                  # 1-3 diagnoses per visit
            dx.append((eid, random.choice(["E11.9", "I10", "J45.909", "N18.3", "F32.9", "M54.5", "Z00.00"])))
with open(out / "encounters.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["encounter_id", "patient_id", "visit_date"]); w.writerows(encounters)
with open(out / "encounter_diagnoses.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["encounter_id", "icd10"]); w.writerows(dx)
rows_visits = len(encounters)
joined = [(e[1], d[1]) for e in encounters for d in dx if d[0] == e[0]]
print("distinct patients:", len({e[1] for e in encounters}))
print("rows in visits table (COUNT(*)):", rows_visits)
print("rows after joining diagnoses (COUNT(*)):", len(joined))
print("patients with 2+ visits:", sum(1 for p in patients if sum(e[1] == p for e in encounters) > 1))
