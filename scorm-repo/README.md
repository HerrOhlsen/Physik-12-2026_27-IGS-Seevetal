# Physik 12 SCORM-Module, IGS Seevetal

SCORM-1.2-Lernpakete für den Physikkurs Jahrgang 12 auf grundlegendem Anforderungsniveau. Ein Modul pro Lernschritt. Aufbau und Build-Mechanik sind identisch zum [Physik Bootcamp](../../physik%20bootcamp/github-repo/README.md), damit nur eine Werkzeugkette gepflegt werden muss.

Abgrenzung: Das **Bootcamp** trainiert Basiskompetenzen (Formeln, Einheiten, Diagramme, Fachsprache) jahrgangsübergreifend. Dieses Repo enthält **Jahrgangsinhalte**. Die Module verlinken bei Lücken in die Bootcamp-Tracks.

## Module

| ModulId | Lernschritt | Status |
|---------|-------------|--------|
| PH12S1Messen | Schwingungen S1: Wovon hängt die Schwingungsdauer ab? | gebaut |
| PH12S2Beschreiben | Schwingungen S2: Die Schwingung als Gleichung | gebaut |
| PH12S3Rechnen | Schwingungen S3: Feder-Masse-Pendel und Fadenpendel | geplant |
| PH12S4Deuten | Schwingungen S4: Energie, Dämpfung, Modellgrenzen | geplant |

## Repo-Struktur

```
scorm-repo/
  src/<ModulId>/      Quellen (index.html + imsmanifest.xml) - hier wird gearbeitet
  modules.json        Mapping ModulId -> ausgelieferte ZIP-Dateinamen
  build.mjs           Baut packages/*.zip deterministisch aus src/
  packages/*.zip      Generiert - NICHT von Hand bearbeiten
.github/workflows/    liegt in der Repo-Wurzel, baut bei jedem Push auf scorm-repo/src/
```

**`src/` ist die einzige Wahrheit.** Die ZIPs in `packages/` werden vollständig daraus generiert. Änderungen direkt an den ZIPs gehen beim nächsten Build verloren.

## Workflow für Änderungen

1. HTML in `src/<ModulId>/index.html` bearbeiten
2. Committen und pushen. Die GitHub Action baut die ZIPs und committet sie automatisch
3. Moodle zieht die neuen Pakete beim nächsten Auto-Update

Lokal bauen: `node build.mjs` oder `node build.mjs PH12S1Messen`

Der Build validiert jedes Modul (Manifest vorhanden und wohlgeformt, `index.html` vollständig, keine Steuerzeichen) und bricht bei Fehlern ab.

## Wichtig: ZIP-Dateinamen sind eingefroren

Moodle lädt die Pakete über feste `raw.githubusercontent.com`-URLs. Die Dateinamen in `packages/` dürfen sich deshalb **nie ändern**, auch wenn sich der Inhalt ändert. Die Versionsgeschichte steckt in git, nicht im Dateinamen.

## Moodle-Integration

Pakete werden als **Download-Pakettyp** eingebunden:

1. Lernpaket im Kurs anlegen, Pakettyp „Download" wählen
2. URL eintragen. Für das erste Modul:

   ```
   https://raw.githubusercontent.com/HerrOhlsen/Physik-12-2026_27-IGS-Seevetal/main/scorm-repo/packages/Physik12-Schwingungen-S1-Messen-v1.0.zip
   ```

3. Auto-Update-Häufigkeit einstellen (Bootcamp: täglich)

Zielkurs: seevetal.moodle-nds.de, Kurs-ID 382 (Abi28 Physik Ohlsen gA), Sektion „Schwingungen".

## Test vor dem Ausliefern

`test/moodle-regressionstest.html` baut die Moodle-Umgebung nach: SCORM-1.2-API mit den
Datentyp-Grenzen, die Moodle durchsetzt, und ein iframe, das mit seinem Inhalt waechst, sodass
das aeussere Dokument scrollt. Genau diese Kombination hat zwei Fehler erzeugt, die beim Testen
ohne LMS unsichtbar bleiben.

```
python -m http.server 8080 --bind 127.0.0.1
```

Dann `http://127.0.0.1:8080/test/moodle-regressionstest.html` oeffnen und auf „Tests ausfuehren"
klicken.

- Anderes Modul: `?modul=../src/PH12S2Beschreiben/index.html` (der Test ist modulunabhängig)
- Anderes Layout: `?layout=popup` (Moodle im neuen Fenster, der Rahmen scrollt selbst) oder
  `?layout=eingebettet` (Rahmen waechst mit dem Inhalt, das aeussere Dokument scrollt).
  Beide pruefen, die Fehlerbilder unterscheiden sich.

Geprueft wird:

1. **Die Ansicht springt beim Abschnittswechsel an den Anfang.**
2. **Der Zustand wird vollstaendig gespeichert.** `cmi.core.lesson_location` fasst nur 255 Zeichen;
   der Zustand gehoert in `cmi.suspend_data` (4096 Zeichen).
3. **`scroll-behavior` erzwingt keine Animation.** Steht es im CSS auf `smooth`, gilt das auch fuer
   `behavior: 'auto'`, und im SCORM-Fenster wird die Animation nicht ausgefuehrt: der Abschnitt
   wechselt, die Ansicht bleibt stehen. Scrollbefehle deshalb immer mit `behavior: 'instant'`.

Wichtig: der Browser-Tab muss im Vordergrund sein, sonst misst der Test kein Layout.

## Was die Module an Moodle melden

- `cmi.core.lesson_status`: `completed`, sobald die Lernenden auf „Lernschritt abschließen" klicken
- `cmi.core.score.raw`: Prozentwert aus dem Selbstcheck am Ende

Der Selbstcheck ist bewusst **nicht** die Leistungsmessung. Die liegt in Brian (`Abschlussquiz: Faden- & Federpendel`). Der Score hier dient nur dazu, dass du im Moodle-Bericht siehst, wer sich überhaupt geprüft hat.

## Rollback

```
git revert <commit>     # einzelne Änderung zurücknehmen
git push                # Moodle zieht den alten Stand beim nächsten Update
```
