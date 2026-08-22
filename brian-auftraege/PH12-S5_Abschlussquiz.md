# Brian-Aktivität: Abschlussquiz Faden- und Federpendel

| | |
|---|---|
| **Aktivitätsname in Brian** | `Abschlussquiz: Faden- & Federpendel` (angelegt) |
| **Typ** | KI-Quiz (Multiple Choice) |
| **Gehört zu** | Abschluss der gesamten Einheit Schwingungen |
| **Kursbereich** | [Schwingungen in Brian](https://student.brian.study/#/courses/14138?highlight-course-unit=28324) |
| **Zeitbedarf** | ca. 20 Minuten |
| **Wann** | etwa eine Woche vor der Klausur |
| **Material mitgeben** | optional die PDFs „Glossar Schwingungen" und „Bewegungsgleichungen von Schwingungen" aus dem Moodle-Kurs |

Anders als die vier Dialog-Aktivitäten ist das hier ein Erstellungs-Prompt: Brian generiert daraus den Fragensatz, den du dann prüfst und freigibst. Das Ergebnis ist die einzige Stelle in der Einheit, an der du systematisch siehst, wo der Kurs vor der Klausur steht.

> [!info] Claude
> Dieser Prompt wurde von Claude erstellt.

---

## Prompt (ab hier kopieren)

Du erstellst Multiple-Choice-Aufgaben für einen Physikkurs. Halte dich genau an die folgenden Vorgaben und stelle keine Rückfragen, bevor du nicht den kompletten Satz Aufgaben geliefert hast.

**Zielgruppe:** Jahrgangsstufe 12 an einer IGS in Niedersachsen, Kurs auf grundlegendem Anforderungsniveau. Die Lernenden sind 17 bis 18 Jahre alt. Viele belegen Physik als Pflichtnaturwissenschaft, das mathematische Niveau ist gemischt. Sie haben die Einheit „Schwingungen" abgeschlossen und bereiten sich auf eine Klausur vor.

**Thema:** mechanische Schwingungen, Faden- und Federpendel.

**Aufgabe:** Erstelle [14] Multiple-Choice-Fragen. Verteile sie so auf die Inhalte:

- 3 Fragen zu den Grundgrößen: Auslenkung, Amplitude, Periodendauer, Frequenz, Zusammenhang f = 1/T
- 3 Fragen zum Ablesen und Deuten von y-t-Diagrammen
- 2 Fragen zur Versuchsplanung und Messgenauigkeit (Variablenkontrolle, Messung über mehrere Perioden)
- 3 Fragen zu den Gleichungen T = 2π·√(l/g) und T = 2π·√(m/D), davon mindestens eine mit einer kleinen Rechnung
- 2 Fragen zur Energieumwandlung beim Schwingen
- 1 Frage zu den Grenzen des Modells (Kleinwinkelnäherung, Dämpfung)

**Aufbau jeder Frage:**

- Genau vier Antwortoptionen A bis D, davon genau eine richtig.
- Formuliere in Alltagssprache. Fachbegriffe nur, wenn sie im Unterricht vorkamen.
- Bei Rechenfragen sollen die Zahlen so gewählt sein, dass man sie im Kopf oder mit wenigen Taschenrechnerschritten schafft.

**Regeln für die falschen Antworten, das ist der wichtigste Teil:**

- Jede falsche Antwort muss eine echte, verbreitete Fehlvorstellung abbilden, nicht offensichtlichen Unsinn. Wer den Inhalt nicht verstanden hat, muss sie für richtig halten können.
- Diese Fehlvorstellungen sollst du gezielt einbauen:
  - Die Amplitude sei der gesamte Abstand zwischen den beiden Umkehrpunkten statt der halbe.
  - Ein schwererer Pendelkörper schwinge langsamer.
  - Eine größere Auslenkung führe zu einer größeren Schwingungsdauer (bei kleinen Winkeln ist das falsch).
  - T und f seien dasselbe oder man müsse multiplizieren statt den Kehrwert zu bilden.
  - Doppelte Fadenlänge ergebe doppelte Schwingungsdauer.
  - Beim Umstellen nach l werde die Wurzel nicht sauber aufgelöst, es entstehe l = g·T/(2π) statt l = g·T²/(4π²).
  - In den Umkehrpunkten sei die Geschwindigkeit maximal.
  - Eine gedämpfte Schwingung werde nicht nur kleiner, sondern auch langsamer in der Periodendauer.
- Alle vier Optionen ungefähr gleich lang. Die richtige Antwort darf nicht die längste oder detaillierteste sein.
- Keine Optionen wie „alle Antworten sind richtig", „keine der genannten" oder Kombinationen wie „A und C".
- Verteile die richtige Antwort gleichmäßig auf die Positionen A bis D, ohne erkennbares Muster.
- Vermeide „immer", „nie", „alle" in falschen Antworten, weil geübte Rater solche Optionen automatisch aussortieren.

**Rückmeldung:** Schreibe zu jeder falschen Antwort einen Hinweis von ein bis zwei Sätzen, der nicht die Lösung verrät, sondern die dahinterliegende Fehlvorstellung aufgreift und zum Nachdenken anstößt. Beispiel für den Ton: „Du hast den ganzen Weg von einem Umkehrpunkt zum anderen genommen. Überlege noch einmal, von wo aus die Amplitude gemessen wird." Zur richtigen Antwort schreibe einen Satz, der die Begründung festigt.

**Ausgabeformat, für jede Frage genau so:**

```
Frage [Nummer]: [Fragetext]
A) [Option]
B) [Option]
C) [Option]
D) [Option]
Richtig: [Buchstabe]
Erklärung: [ein Satz]
Hinweis zu [falscher Buchstabe]: [ein bis zwei Sätze]
Hinweis zu [falscher Buchstabe]: [ein bis zwei Sätze]
Hinweis zu [falscher Buchstabe]: [ein bis zwei Sätze]
```
