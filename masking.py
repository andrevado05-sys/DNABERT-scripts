import os

def seq_to_kmers(seq, k=6):
 
    return [seq[i:i+k] for i in range(len(seq) - k + 1)]

def process_and_mask(file_name, label):
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    input_path = os.path.join(desktop, file_name)
    
    if not os.path.exists(input_path):
        print(f"File non trovato: {file_name}. Assicurati che sia sul Desktop!")
        return

    with open(input_path, 'r') as f:
        entries = f.read().split(">")[1:]

    results = {"inizio": [], "centro": [], "fine": []}

    for entry in entries:
        lines = entry.strip().split("\n")
        seq = "".join(lines[1:]).upper().replace(" ", "")
        if not seq: continue
        
        kmers = seq_to_kmers(seq)
    
        m_inizio = ["[MASK]"] * 15 + kmers[15:]
        results["inizio"].append(" ".join(m_inizio))
        

        m_centro = kmers[:220] + ["[MASK]"] * 15 + kmers[235:]
        results["centro"].append(" ".join(m_centro))
        
        m_fine = kmers[:-15] + ["[MASK]"] * 15
        results["fine"].append(" ".join(m_fine))

    # Salvataggio dei file risultati sul Desktop
    for pos, data in results.items():
        out_name = f"DNABERT_test_{label}_{pos}.txt"
        with open(os.path.join(desktop, out_name), 'w') as out:
            out.write("\n".join(data))
        print(f"Creato: {out_name}")

# Esecuzione per entrambi i tuoi file
process_and_mask("tatahg38_fYp4B.fa.txt", "TATA")
process_and_mask("notatahg38_KzawA.fa.txt", "noTATA")