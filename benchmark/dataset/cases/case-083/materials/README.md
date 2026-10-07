# Image-edit annotation prototype
We want the rate and spatial distribution of unintended edits, separately from requested changes. Participants view the original and edited illustration, choose Yes/No/Cannot judge, and mark unintended-change regions when Yes. Each region is stored as x, y, width, height relative to the edited image, normalized into [0,1] so the aggregation job can combine images with different resolutions. The existing analysis consumes those normalized coordinates. Keep the task and stored field meanings stable.

Open index.html in a browser or run python3 -m http.server 8000 here. Drag from any corner to another to draw a region; Clear regions resets boxes. Records save only to localStorage and are shown below the form. The original SVGs are actual illustrative stimuli, not photographs or validated human test items. No external service, recruitment or payment is connected. One demonstration image is supplied; this repository does not specify a population-level stimulus sample.

## Export note
The rendering/response implementation app.js was omitted from this export. Its behavior cannot be established from the remaining template. Request that file or an interaction trace before concluding how the deployed form behaves.
