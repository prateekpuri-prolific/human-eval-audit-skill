# Multi-turn reply evaluation
The primary measure is preference for a helpful next reply conditioned on the complete preceding conversation. Earlier constraints remain relevant unless the user retracts them. Participants should receive all preceding turns supplied in the item. Responses are A, B, Tie, or Cannot judge. Preserve these output codes and the original dialogue; this is preference collection, not a keyed attention check.

Open index.html directly or serve this directory with python3 -m http.server 8000. data.js is an original demonstration item; app.js renders it. Records are stored only on the local device and shown under the form. No production service, participant assignment or payment logic is included. The demonstration checks the local implementation; it does not establish broad model quality or a population preference distribution.

## Export note
The rendering/response implementation app.js was omitted from this export. Its behavior cannot be established from the remaining template. Request that file or an interaction trace before concluding how the deployed form behaves.
