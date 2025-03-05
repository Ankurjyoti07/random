import re

def extract_citations(tex_file):

    with open(tex_file, "r", encoding="utf-8") as file:
        tex_content = file.read()

    citation_keys = set(re.findall(r"\\cite[tp]?\{([^}]+)\}", tex_content))
    citations = set()
    for keys in citation_keys:
        citations.update(key.strip() for key in keys.split(","))
    return citations

def extract_bib_entries(bib_file):

    with open(bib_file, "r", encoding="utf-8") as file:
        bib_content = file.read()

    entries = re.findall(r"(@\w+\{([^,]+),.*?\n\})", bib_content, re.DOTALL)
    bib_entries = {key: entry for entry, key in entries}
    return bib_entries

def generate_ref_bib(tex_file, bib_file, output_file="ref.bib"):

    used_citations = extract_citations(tex_file)
    all_bib_entries = extract_bib_entries(bib_file)

    with open(output_file, "w", encoding="utf-8") as file:
        for citation in used_citations:
            if citation in all_bib_entries:
                file.write(all_bib_entries[citation] + "\n\n")

    print(f"Generated {output_file} with {len(used_citations)} entries.")

'''
example usage: generate_ref_bib("paper.tex", "biblio.bib")
returns: ref.bib file with ref entries
'''