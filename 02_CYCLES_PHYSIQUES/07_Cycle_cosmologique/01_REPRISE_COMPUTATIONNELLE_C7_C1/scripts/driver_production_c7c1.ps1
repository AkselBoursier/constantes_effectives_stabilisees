<#
    C7-C1 — driver de lancement durci (porte REJ-1, issues #94 et #63).

    Trois règles absolues, payées par les incidents SENT-0E/F :

      1. AUCUN timeout, d'aucune sorte. Ce script ne borne JAMAIS la durée
         du processus scientifique ; le silence de Cobaya n'est JAMAIS une
         condition d'arrêt (leçon attempt1 : kill par timeout de harnais).
         L'attente est WaitForExit() sans argument : illimitée.

      2. JAMAIS de console pour le processus scientifique. Sa sortie va
         dans un JOURNAL FICHIER ; sans console, le gel par sélection
         QuickEdit (leçon attempt3) est structurellement impossible. Ce
         driver lui-même n'écrit RIEN sur la console : toute sa narration
         va dans son propre journal. Surveiller avec :
             Get-Content <journal> -Wait

      3. AUCUNE relance automatique. Une exécution = une commande humaine.
         Si le processus meurt, ce driver consigne et se termine ; il ne
         relance rien, jamais.

    Ce fichier est PUBLIC : il ne contient aucun chemin local réel. Tout
    chemin vient de l'enveloppe privée (variables C7C1_*) déjà activée
    dans la session, ou des paramètres passés à l'invocation.

    Usage (session où l'enveloppe C7-C1 est activée) :

      pwsh -NoProfile -File scripts\driver_production_c7c1.ps1 `
          -Mode produire -Variante M2a-N -Graine 630101 `
          -Autorisation <fichier privé> -Franchissement <référence> `
          -PythonDirecteur <python de l'environnement directeur>

      (mode reprendre : ajouter -RatificationReprise <référence> ;
       exige le lanceur post-REC-1)

    Fin de vie du journal : la sortie du processus est d'abord captée dans
    le sous-arbre temporaire reconnu (_tmp), puis AJOUTÉE (append, jamais
    d'écrasement) à chain.console.log DANS le répertoire du run une fois
    le processus terminé — jamais pendant : le répertoire du run n'est
    créé que par l'acquisition exclusive du lanceur (B1), et rien n'y
    écrit d'autre que le lanceur tant qu'il vit.
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory)][ValidateSet('produire', 'reprendre')]
    [string]$Mode,
    [Parameter(Mandatory)][string]$Variante,
    [Parameter(Mandatory)][int]$Graine,
    [Parameter(Mandatory)][string]$Autorisation,
    [Parameter(Mandatory)][string]$Franchissement,
    [string]$RatificationReprise,
    [Parameter(Mandatory)][string]$PythonDirecteur,
    [string]$ScriptLanceur = 'scripts\run_mcmc_xz_g2_4.py'
)

$ErrorActionPreference = 'Stop'

# ---------------------------------------------------------------- refus
if ($PSVersionTable.PSVersion.Major -lt 7) {
    throw 'pwsh 7+ requis (PowerShell 5.1 a déjà tué un driver en silence)'
}
foreach ($v in 'C7C1_XZ_OUT_DIR', 'C7C1_CONTRAT_LOCAL', 'C7C1_DATA_DIR') {
    if (-not (Get-Item "env:$v" -ErrorAction SilentlyContinue)) {
        throw "enveloppe non activée : variable $v absente"
    }
}
if (-not (Test-Path $PythonDirecteur)) {
    throw 'Python directeur introuvable'
}
if (-not (Test-Path $ScriptLanceur)) {
    throw "lanceur introuvable : $ScriptLanceur (lancer depuis la racine C7-C1)"
}
if ($Mode -eq 'reprendre' -and -not $RatificationReprise) {
    throw 'mode reprendre : -RatificationReprise est obligatoire'
}

# ------------------------------------------------------------- identités
$horoUtc  = (Get-Date).ToUniversalTime().ToString('yyyyMMddTHHmmssZ')
$runRel   = "g2_4/P_WS/$Variante/s$Graine"
$runDir   = Join-Path $env:C7C1_XZ_OUT_DIR ($runRel -replace '/', '\')
$staging  = Join-Path $env:TMP "driver_c7c1_$horoUtc"
New-Item -ItemType Directory -Force $staging | Out-Null
$journalDriver = Join-Path $staging 'driver.log'
$journalOut    = Join-Path $staging 'chain.console.out.log'
$journalErr    = Join-Path $staging 'chain.console.err.log'

function Consigner([string]$m) {
    Add-Content -Path $journalDriver -Encoding UTF8 -Value (
        '{0} {1}' -f (Get-Date).ToUniversalTime().ToString(
            'yyyy-MM-ddTHH:mm:ssZ'), $m)
}

# ------------------------------------------------------------- arguments
$argsLanceur = @('-u', $ScriptLanceur)
if ($Mode -eq 'produire') {
    $argsLanceur += @('--produire', $Variante, "$Graine",
                      '--je-confirme-la-production')
} else {
    $argsLanceur += @('--reprendre', $Variante, "$Graine",
                      '--je-confirme-la-reprise',
                      '--ratification-reprise', $RatificationReprise)
}
$argsLanceur += @('--autorisation', $Autorisation,
                  '--franchissement-sent0d', $Franchissement)

# ------------------------------------------------------------- lancement
Consigner "driver REJ-1 : mode=$Mode variante=$Variante graine=$Graine"
Consigner "journal du driver : $journalDriver"
Consigner 'methode : Start-Process detache, sans console, sans timeout'
$proc = Start-Process -FilePath $PythonDirecteur `
    -ArgumentList $argsLanceur `
    -WorkingDirectory (Get-Location).Path `
    -WindowStyle Hidden `
    -RedirectStandardOutput $journalOut `
    -RedirectStandardError $journalErr `
    -PassThru
Consigner "processus scientifique lance : PID=$($proc.Id) UTC=$horoUtc"
Consigner "surveiller : Get-Content '$journalOut' -Wait"

# Attente ILLIMITEE, par contrat : WaitForExit() SANS argument — la forme
# WaitForExit(millisecondes) serait un timeout et est interdite ici.
# Aucune borne, aucune relance. Tuer ce driver ne tue pas le processus
# scientifique (detache), et un processus deja termine ne fait pas
# echouer l'attente.
$proc.WaitForExit()
$codeSortie = $proc.ExitCode
Consigner ('processus scientifique termine : PID={0} code={1} UTC={2}' -f
    $proc.Id, $codeSortie,
    (Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ'))

# ------------------------------------------- consolidation post-mortem
# Append SEULEMENT : un chain.console.log existant (tentative ou reprise
# anterieure) n'est jamais ecrase ni tronque.
if (Test-Path $runDir) {
    $cible = Join-Path $runDir 'chain.console.log'
    Add-Content -Path $cible -Encoding UTF8 -Value (
        "===== lancement $horoUtc PID=$($proc.Id) mode=$Mode " +
        "code_sortie=$codeSortie =====")
    foreach ($j in @($journalOut, $journalErr)) {
        if ((Test-Path $j) -and (Get-Item $j).Length -gt 0) {
            Add-Content -Path $cible -Encoding UTF8 -Value (
                '----- {0} -----' -f (Split-Path $j -Leaf))
            Get-Content $j -Encoding UTF8 | Add-Content -Path $cible -Encoding UTF8
        }
    }
    Remove-Item $journalOut, $journalErr -ErrorAction SilentlyContinue
    Consigner "journal consolide (append) : $cible"
} else {
    Consigner ('repertoire du run absent (arret avant acquisition) : ' +
               'journaux conserves dans le staging pour audit')
}
Consigner 'driver termine — AUCUNE relance automatique, par contrat'
exit $codeSortie
