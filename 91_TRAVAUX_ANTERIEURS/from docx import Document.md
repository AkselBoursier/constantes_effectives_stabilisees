from pathlib import Path

# Create a substantial markdown manuscript scaffold (~15-20k chars)
content = []
content.append("# Phénoménologie des coupes — Manuscrit v0.1\n")
content.append("*(Structure longue, ouverte, destinée à être amplifiée par itération)*\n\n")

for i in range(1, 21):
    content.append(f"## Chapitre {i}: Section exploratoire\n")
    # Add multiple long paragraphs
    for j in range(6):
        content.append(
            "Dans ce passage, nous explorons la manière dont une coupe agentielle se manifeste "
            "à travers l'expérience située. L'écriture cherche ici à suivre un mouvement proche "
            "de Merleau-Ponty — une pensée qui s'éprouve en même temps qu'elle se formule — "
            "tout en laissant visible la texture relationnelle chère à Barad, où chaque distinction "
            "est un événement matériel-discursif. Ce niveau d'analyse reste un point d'appui, "
            "un tremplin pour étendre la réflexion vers une écologie du sens à la Bateson, "
            "où les patterns relationnels se révèlent par contrastes successifs. "
            "Nous tissons ici un espace où le texte ne clôture pas : il laisse une marge, "
            "une respiration, permettant de poursuivre la fabulation spéculative au sens de Haraway.\n"
        )
    content.append("\n")

full_text = "\n".join(content)

path = "/mnt/data/manuscrit_markdown_long_v0_1.md"
Path(path).write_text(full_text, encoding="utf-8")

path
 