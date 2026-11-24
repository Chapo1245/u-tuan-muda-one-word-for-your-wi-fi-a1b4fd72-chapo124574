# REPORT — One Word for Your Wi-Fi

- **Competition:** u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72 — One Word for Your Wi-Fi
- **Prize:** $2, winner-takes-all (1st place). **Deadline: 28 Nov 2026 18:35 WIB.**
- **Repo:** Chapo1245/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72-chapo124574
- **Entry program:** `main.py` (Python 3.13, stdlib only) writes one word to `/output/entry.txt`.

## Chosen word

**Moody** (5 characters, 5 bytes)

## Candidate words (reasoned pairwise)

1. **Moody** — personifies the router as a moody housemate: fine one minute,
   sulking the next, for no reason. Funny at once, instantly readable, and
   true to how home Wi-Fi actually behaves. Surprising angle: not speed,
   but temperament.
2. **Dramatic** — Wi-Fi that drops at the climax of a show or mid-sentence on
   a call. Funny and true, but it describes the timing of the failure, not
   the Wi-Fi itself; slightly narrower than Moody, and longer (8 bytes).
3. **Fickle** — Wi-Fi that won't stay committed to a connection. Accurate and
   short (6 bytes), but the laugh is thinner: it reads as a vocabulary word
   rather than a lived joke, and it needs a half-second more to land.

## Pairwise judgement (against the judge brief)

- Moody vs Fickle: Moody wins — bigger immediate laugh (personification),
  equally true, more instantly readable.
- Moody vs Dramatic: Moody wins — covers the everyday lived experience
  (fine in the morning, dead by evening), not just bad timing; also shorter,
  which matters on the exact-tie break (fewer bytes wins).
- Against the obvious clichés (Slow, Laggy, Buffering, Loading, Offline):
  all three candidates beat them on freshness (criterion 4) — the clichés
  are what everyone reaches for. Moody beats them on the laugh too, because
  it reframes the annoyance instead of just naming the symptom.

## Verification (local)

- `python3 main.py` run twice; `/output/entry.txt` byte-identical both runs.
- Content: exactly `Moody`, 5 characters, single word, UTF-8, within the
  1–20 character gate.
