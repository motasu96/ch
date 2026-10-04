# جميع Prompts الصور — مرتبة

> مُستخرجة آليًا من [`01_BLUEPRINT.md`](01_BLUEPRINT.md). 28 لقطة مولّدة. المشاهد 04 و06 أرشيف حقيقي، و05 و18 Motion Graphics — لا Prompts توليد لها عمدًا.

## إعدادات عامة لكل الأدوات

| الأداة | الإعداد المقترح |
|---|---|
| Midjourney | `--ar 16:9 --style raw --stylize 50-100` + `--oref`/`--cref` للشخصيات + `--no` للسلبيات |
| Flux / Flux Kontext | 16:9 (مثلًا 1920×1080 أو 1344×768)، Guidance منخفض-متوسط، مرجع صورة للشخصية |
| Imagen / Ideogram / غيرها | 16:9، Photorealistic، Negative prompt في الحقل المخصص |

- استخدم **أداة واحدة** لكامل الفيلم، واحفظ الـ Seed لكل لقطة معتمدة.
- ولّد 4–8 نسخ لكل لقطة واختر الأقل "مثالية" والأكثر واقعية.
- افحص اليدين والعينين والنصوص الخفية قبل الاعتماد.

## Negative Prompt الموحّد (NEG-IMAGE)

```text
cartoon, anime, illustration, 3D render, CGI, video game graphics, plastic skin, artificial face, deformed face, distorted anatomy, extra fingers, missing fingers, malformed hands, duplicated people, duplicated objects, unnatural eyes, asymmetrical face, unrealistic skin, oversaturated colors, excessive HDR, fantasy architecture, generic Middle Eastern stereotypes, fake historical costumes, text, subtitles, captions, logo, watermark, blurry face, low resolution, excessive sharpening, unrealistic motion, melting objects, warped buildings, distorted background, airbrushed skin, beauty filter, glamour lighting, studio lighting, desert dunes, camels, Gulf-style architecture, Moroccan architecture, flags, political posters, graffiti slogans, weapons, soldiers, blood, injuries
```

---

### 01A — المشهد 01: الفجر

**Prompt**

```text
Cinematic documentary photograph, extreme wide establishing shot of a quiet Palestinian hill village in the central West Bank highlands at first light, about ten minutes before sunrise. Clusters of old cream-and-honey limestone houses with arched windows, flat roofs and a few small domes stacked along a terraced hillside; dry-stone terrace walls lined with ancient gnarled olive trees in the foreground; a modest stone minaret rising among the roofs; a few black rooftop water tanks; a single warm window light still on. Weather: clear and still, thin layers of low morning mist resting in the valley, pale blue-to-apricot sky gradient, no visible sun disc yet. Lighting: soft indirect dawn skylight, a gentle warm rim along the ridge line, deep but readable shadows. Camera at eye level from the opposite hillside, 35mm cinema prime on ARRI Alexa Mini LF, rule-of-thirds composition with the village on the right third and olive branches framing the lower-left foreground, deep focus with natural atmospheric falloff. No people. Restrained documentary color grade, muted olive greens, warm limestone highlights, slightly lifted shadows, Kodak Vision3 250D film emulation, subtle 35mm film grain, natural high dynamic range without halos, photorealistic, authentic Palestinian architecture, serene and contemplative, 16:9, no text, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
people, cars, modern high-rise buildings, sun disc, lens flare, fog too dense, snow
```

---

### 02A — المشهد 02: التراب والزيتون

**Prompt**

```text
Cinematic documentary macro photograph of the weathered hands of an 86-year-old Palestinian man scooping and loosely holding a handful of dark red-brown terra rossa soil in an olive grove. Large knotted fingers, prominent veins, age spots, deep creases filled with fine soil, short clean nails, a plain thin silver ring on the right ring finger; the cuff of a charcoal-grey wool jacket and a faded beige shirt sleeve visible at the frame edge. Location: a terraced olive grove in the Palestinian central highlands, early morning just after sunrise, clear weather. Lighting: low warm side light from the left raking across the skin and soil grains, soft natural fill, gentle glow in the background. Shot with a 100mm macro lens on ARRI Alexa Mini LF, camera slightly above at a 30-degree angle, hands centered in the lower two-thirds of the frame, very shallow depth of field with the background dissolving into soft olive-green and gold bokeh. Natural skin texture with pores and fine wrinkles, tactile and intimate, restrained documentary color grade, Kodak Vision3 250D emulation, subtle 35mm grain, photorealistic, no CGI, 16:9, no text, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
gloves, dirty nails exaggerated, manicured hands, young hands, sand instead of soil, young sapling, plastic plants
```

---

### 02B — المشهد 02: التراب والزيتون

**Prompt**

```text
Cinematic documentary photograph of a single ancient Palestinian olive tree with a massive, hollowed, twisted trunk split into several sculptural sections and a silver-green canopy above, standing on a stone terrace in an olive grove in the hills near Bethlehem, morning sunlight. Low-angle medium-wide shot from near the base, 35mm prime lens, the trunk filling the left two-thirds of the frame, the canopy cut by the top edge, soft sun flare filtering through leaves at the upper right. Reddish soil, dry grass and scattered limestone rocks around the roots, a dry-stone terrace wall behind. Clear sky with light haze. Natural warm morning light, deeply textured bark, moderate depth of field with the background grove gently out of focus. Restrained grade with muted silvery greens and warm earth tones, Kodak Vision3 250D emulation, fine film grain, natural dynamic range, photorealistic, timeless and dignified, no people, 16:9, no text, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
gloves, dirty nails exaggerated, manicured hands, young hands, sand instead of soil, young sapling, plastic plants
```

---

### 03A — المشهد 03: إيقاع الحياة

**Prompt**

```text
Cinematic documentary photograph of an 80-year-old Palestinian grandmother baking flatbread in a traditional clay taboun oven in the small stone courtyard of a village house, early morning. She has a round kind face, deep wrinkles and soft brown eyes, a loose white cotton headscarf, and wears a traditional black thobe with deep-red cross-stitch tatreez embroidery on the chest panel, sleeves pushed to the forearms. She lifts a freshly baked, blistered round of taboun bread with her fingertips, focused and calm, with a faint satisfied expression. A low smoke-darkened clay oven at waist level, a wooden board with dough balls dusted with flour, a metal bowl, olive-wood sticks stacked beside her, a limestone wall with a small grapevine. Lighting: low warm sunlight entering from a courtyard opening on the right, soft wisps of smoke catching the light, natural fill bouncing from a whitewashed wall. Medium shot at seated eye level, 50mm prime lens, shallow depth of field, subject on the left third. Natural skin texture, real fabric weave and embroidery detail, restrained warm documentary grade, Kodak Vision3 250D emulation, subtle grain, photorealistic, unposed and authentic, 16:9, no text, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
period costume, Ottoman costume, fez, staged smiles at camera, modern gas oven, metal oven, plastic toys, tourists
```

---

### 03B — المشهد 03: إيقاع الحياة

**Prompt**

```text
Cinematic documentary photograph of a 46-year-old Palestinian farmer working the soil between olive trees on a stone-walled terrace with a short-handled hoe, mid-morning. Medium-stocky build, sun-tanned skin, short black hair greying at the temples, short dark beard with grey streaks, calm focused expression; faded olive-green work jacket over a blue-grey checkered flannel shirt, worn jeans, dusty brown work boots. Terraced hills dotted with olive and almond trees descend into a valley, scattered limestone houses on the opposite slope. Clear sky with light haze, warm light from a 35-degree sun angle, soft shadows. Medium-wide shot at eye level, 35mm prime lens, the farmer on the right third mid-swing, the terrace wall leading the eye diagonally, moderate depth of field. Restrained documentary grade, muted greens and warm earth tones, Kodak Vision3 250D emulation, subtle grain, natural skin texture, photorealistic, 16:9, no text, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
period costume, Ottoman costume, fez, staged smiles at camera, modern gas oven, metal oven, plastic toys, tourists
```

---

### 03C — المشهد 03: إيقاع الحياة

**Prompt**

```text
Cinematic documentary photograph of three Palestinian village children aged about 8 to 11 running and laughing down a narrow sloping alley of old limestone houses with arched doorways, worn stone steps, potted geraniums and a climbing grapevine overhead, morning. Leading the group is a 10-year-old boy with short dark-brown wavy hair, light olive skin and large dark eyes, wearing a light-blue collared shirt and navy-blue trousers; the other two children wear ordinary modern clothes in muted colors. Shafts of warm sunlight cut across the alley, the rest in soft shade. Shot from a low angle at the bottom of the alley, 35mm prime lens, children mid-stride with slight natural motion blur at the feet, moderate depth of field. Candid, joyful but natural, not staged, realistic child proportions, natural skin texture, restrained documentary grade, Kodak Vision3 250D emulation, subtle grain, photorealistic, 16:9, no text, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
period costume, Ottoman costume, fez, staged smiles at camera, modern gas oven, metal oven, plastic toys, tourists
```

---

### 07A — المشهد 07: الطريق (مشهد تمثيلي)

**Prompt**

```text
Cinematic documentary reconstruction photograph, close low-angle shot at ground level of the feet of a rural family walking away along a dusty unpaved country road: an adult woman's feet in worn leather sandals beneath the dark hem of a long embroidered dress, an adult man's feet in old scuffed leather shoes, and a small boy's feet in simple sandals, all walking away from the camera. At the top edge of the frame, the boy's small hand holds the woman's hand. A cloth bundle tied with rope hangs from the man's hand. No faces visible. Late afternoon, overcast autumn sky, diffused cool light, soft dust lifting from the road. 35mm prime lens at road level, shallow depth of field, feet sharp, the road and dry hills receding into soft focus. Muted, heavily desaturated color grade with cool shadows, almost colorless but not black and white, Kodak Vision3 film emulation, visible fine film grain, photorealistic, quiet and dignified, no violence, 16:9, no text, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
visible faces, crying faces, soldiers, weapons, trucks, tanks, explosions, smoke, burning houses, modern clothing, sneakers, plastic bags, black-and-white archival imitation, sepia fake photo
```

---

### 07B — المشهد 07: الطريق (مشهد تمثيلي)

**Prompt**

```text
Cinematic documentary reconstruction photograph, extreme wide shot of a small rural family seen from behind, walking away along a winding dirt road that crosses bare rolling hills at dusk under a heavy overcast sky. Five small figures: a man carrying a cloth bundle on his shoulder, a woman balancing a bundle on her head, an elderly woman, and two children, the smaller boy holding the woman's hand. The figures are small in the lower third of the frame, faces not visible, simple dark rural clothing in muted tones. A lone olive tree on the left, distant hills fading into haze. Cold, diffused, low-contrast light, a muted desaturated palette leaning toward grey-green and dust, 50mm lens from a slightly elevated position, deep focus. Fine film grain, photorealistic, restrained and humane, no violence, no soldiers, no vehicles, 16:9, no text, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
visible faces, crying faces, soldiers, weapons, trucks, tanks, explosions, smoke, burning houses, modern clothing, sneakers, plastic bags, black-and-white archival imitation, sepia fake photo
```

---

### 08A — المشهد 08: المفتاح

**Prompt**

```text
Cinematic documentary macro photograph of an old hand-forged iron house key, about 15 centimeters long, with a large oval bow, a long shaft and a simple rectangular bit, dark patina with traces of rust, worn smooth where generations of fingers held it, resting diagonally across the open palm of an 86-year-old Palestinian man. His palm is deeply lined, with a plain thin silver ring on the right ring finger and the cuff of a charcoal-grey wool jacket at the frame edge. Interior of a modest village home, soft late-afternoon window light from the left, warm dust particles floating in the beam, dark warm background falling into shadow. 100mm macro lens, camera slightly above the palm, key positioned diagonally from lower left to upper right, extremely shallow depth of field with the key's bit in razor-sharp focus. Rich tactile textures of iron and skin, restrained warm grade with deep but clean shadows, Kodak Vision3 500T emulation, subtle grain, photorealistic, intimate and reverent, 16:9, no text, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
tears, crying, theatrical sadness, modern key, Yale key, keyring, key changing shape, keffiyeh on head, young man, clean smooth skin
```

---

### 08B — المشهد 08: المفتاح

**Prompt**

```text
Cinematic documentary portrait of an 86-year-old Palestinian man sitting by a window inside his modest stone home, holding an old hand-forged iron key with a large oval bow loosely against his chest. Lean build, deeply lined sun-weathered olive-brown skin, short neatly trimmed white beard, thin white hair, warm dark-brown eyes with slight age clouding looking off-camera toward the window, a quiet, composed expression of memory, no tears. A white-and-black checkered keffiyeh draped loosely over his shoulders, charcoal-grey wool jacket over a faded beige collarless shirt, a plain thin silver ring on his right ring finger. Background: a whitewashed wall softly out of focus with a small framed faded photograph and an old wooden cabinet. Lighting: soft late-afternoon window light from camera left, gentle Rembrandt light on the face, deep warm falloff. Medium close-up at eye level, 85mm prime lens, shallow depth of field, eyes in critical focus, subject on the right third looking into the frame. Natural skin texture with pores, wrinkles and slight imperfections, restrained warm grade, Kodak Vision3 500T emulation, subtle grain, photorealistic, dignified, 16:9, no text, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
tears, crying, theatrical sadness, modern key, Yale key, keyring, key changing shape, keffiyeh on head, young man, clean smooth skin
```

---

### 09A — المشهد 09: الذاكرة

**Prompt**

```text
Cinematic documentary close-up of elderly hands slowly turning the thick black cardboard pages of an old family photo album resting on a worn wooden table, beside a small glass of tea. The album holds small vintage black-and-white and sepia photographs with deckled white borders held by paper photo corners; the photographs are softly out of focus so that no faces can be read. The hands belong to an 86-year-old man, with a plain thin silver ring on the right ring finger and a charcoal-grey wool jacket cuff. Soft late-afternoon window light from the left, warm and gentle, dust in the air. Camera at a 45-degree high angle, 50mm prime lens, shallow depth of field with focus on the fingertips and the page edge. Worn paper textures, restrained warm grade, Kodak Vision3 500T emulation, subtle grain, photorealistic, quiet and intimate, 16:9, no text, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
readable faces in photos, sharp faces in photos, modern color photos, smartphone, graffiti, flags, people in ruins, horror atmosphere, dramatic storm
```

---

### 09B — المشهد 09: الذاكرة

**Prompt**

```text
Cinematic documentary photograph of the roofless ruins of an old limestone village house on a hillside, its arched doorway still standing, overgrown with wild grass and fig shoots, with a large clump of prickly pear cactus in the soft foreground; scattered dressed stones on the ground; olive and almond trees growing wild around it; distant hills under a soft overcast late-afternoon sky. Medium-wide shot at eye level through the out-of-focus cactus pads, 35mm prime lens, the arched doorway on the right third, moderate depth of field. Cool, quiet, slightly desaturated grade, muted greens and pale stone, Kodak Vision3 250D emulation, fine film grain, photorealistic, contemplative, no people, no graffiti, no flags, 16:9, no text, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
readable faces in photos, sharp faces in photos, modern color photos, smartphone, graffiti, flags, people in ruins, horror atmosphere, dramatic storm
```

---

### 10A — المشهد 10: الأجيال الجديدة

**Prompt**

```text
Cinematic documentary photograph of a 10-year-old Palestinian boy walking to school along a quiet village road in the early morning, seen in a three-quarter front view. Slim, light olive skin, short dark-brown wavy hair, large dark eyes, a curious, alert, slightly sleepy expression; light-blue collared shirt, navy-blue trousers, scuffed white sneakers, a worn dark-blue backpack with one frayed strap. The road is lined with a low dry-stone wall, olive trees and a few limestone houses with black water tanks on their roofs; two other schoolchildren walk in the distance. Clear weather, low warm morning sun backlighting his hair, soft natural fill. Medium-wide shot at the child's eye level, 35mm prime lens, the boy on the left third walking into the frame, shallow-to-moderate depth of field. Natural skin texture, realistic child proportions, restrained documentary grade, Kodak Vision3 250D emulation, subtle grain, photorealistic, hopeful and ordinary, 16:9, no text, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
school uniform logos, readable writing on board, girls in boys classroom inconsistently, modern luxury school, computers everywhere, posed group photo, children looking at camera
```

---

### 10B — المشهد 10: الأجيال الجديدة

**Prompt**

```text
Cinematic documentary photograph inside a simple Palestinian public school classroom for boys: about twenty boys aged 9 to 11 sitting at worn wooden two-seat desks, a few raising their hands, one reading aloud from a textbook; in the second row a 10-year-old boy with short dark-brown wavy hair, light olive skin and a light-blue collared shirt smiles at the classmate beside him. Pale-green painted walls, a large green chalkboard with chalk marks blurred and unreadable, metal-framed windows letting in bright soft daylight from the left, children's drawings pinned on the wall slightly out of focus. Eye-level medium-wide shot from the side of the room, 35mm prime lens, moderate depth of field, the boy in sharp focus. Lively and natural, realistic faces with diverse features, natural skin texture, restrained documentary grade, subtle grain, photorealistic, 16:9, no readable text, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
school uniform logos, readable writing on board, girls in boys classroom inconsistently, modern luxury school, computers everywhere, posed group photo, children looking at camera
```

---

### 11A — المشهد 11: الزيتون

**Prompt**

```text
Cinematic documentary photograph of a Palestinian family olive harvest in an autumn grove on terraced hills: a 46-year-old farmer with short black hair greying at the temples and a short dark beard with grey streaks, wearing a faded olive-green work jacket over a blue-grey checkered flannel shirt, stands on a short wooden ladder combing olives from the branches with his hands; below him, on large tarps spread over the red soil, two women in headscarves and simple work clothes and a 10-year-old boy in a light-blue collared shirt gather fallen olives into buckets and woven sacks. Mid-morning, clear autumn sky, warm low sun filtering through the silver-green leaves, dappled light on the tarps. Medium-wide shot at eye level, 35mm prime lens, the farmer on the upper right third, the family in the lower-left foreground, moderate depth of field. Green and black olives clearly visible, realistic tools, natural candid poses, natural skin texture, restrained warm documentary grade, Kodak Vision3 250D emulation, subtle grain, photorealistic, 16:9, no text, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
machinery, tractors, olive shaking machine, perfect identical olives, plastic fruit, spring blossoms, green summer grass
```

---

### 11B — المشهد 11: الزيتون

**Prompt**

```text
Cinematic documentary macro photograph of a farmer's strong, sun-tanned, work-worn hands holding a cupped handful of freshly picked green and purple-black olives with a few silver-green leaves, above a tarp covered with olives. The cuff of a faded olive-green jacket and a blue-grey checkered shirt cuff are visible. Autumn morning light from behind and the side, backlit leaves glowing, warm highlights on the glossy olive skins. 100mm macro lens, shallow depth of field, hands centered, a background of olive branches in soft bokeh. Natural skin texture with small cuts and calluses, restrained warm grade, subtle grain, photorealistic, 16:9, no text, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
machinery, tractors, olive shaking machine, perfect identical olives, plastic fruit, spring blossoms, green summer grass
```

---

### 12A — المشهد 12: المدينة

**Prompt**

```text
Cinematic documentary photograph of a busy street in the old commercial center of a Palestinian West Bank city such as Nablus, late morning: a covered stone market passage with high vaulted arches opening onto a sunlit street, shopfronts with sacks of spices, trays of knafeh, hanging clothes, a man pushing a hand cart, shoppers of all ages in modern everyday clothes, some women in headscarves and some without, a few young men with backpacks. Shop signs present but blurred and unreadable. Hazy sunlight spilling through the arch opening, warm stone tones, mixed shade. Eye-level medium-wide shot, 35mm lens, layered composition with foreground figures slightly out of focus, natural motion blur on a passer-by. Authentic, lively, everyday, not exoticized, natural skin textures, restrained documentary grade, subtle grain, photorealistic, 16:9, no readable text, no logos, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
readable Arabic signs, misspelled signage, brand logos, Gulf malls, skyscrapers, palm-lined boulevards, exoticized bazaar, belly dancers, hookah cliché focus
```

---

### 12B — المشهد 12: المدينة

**Prompt**

```text
Cinematic documentary photograph of young Palestinians in their twenties at a small sidewalk café in Ramallah in the early evening: two young women and two young men around a small table with cups of coffee and tea, one laughing, one looking at a phone, one gesturing in conversation; casual modern clothing, one of the women wears a headscarf and the other does not. Behind them a sloping street with parked cars, limestone-clad buildings, warm shop lights turning on and a soft dusk sky. Medium shot from across the table at seated eye level, 50mm prime lens, shallow depth of field, a natural candid moment. Natural skin textures, realistic faces, restrained warm grade, Kodak Vision3 500T emulation, subtle grain, photorealistic, 16:9, no readable text, no logos, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
readable Arabic signs, misspelled signage, brand logos, Gulf malls, skyscrapers, palm-lined boulevards, exoticized bazaar, belly dancers, hookah cliché focus
```

---

### 12C — المشهد 12: المدينة

**Prompt**

```text
Cinematic documentary photograph, wide view over the rooftops of a Palestinian hill city such as Bethlehem at golden hour: dense limestone buildings of different ages climbing the slopes, rooftops crowded with black water tanks, solar water heaters and satellite dishes, a few minarets and a church bell tower on the skyline, laundry on a line, pigeons in flight, surrounding hills with olive groves fading into warm haze. Elevated viewpoint, 50mm lens compressing the layers, deep focus. Warm low sun from the right, long soft shadows. Restrained warm, natural grade, Kodak Vision3 250D emulation, subtle grain, photorealistic, 16:9, no text, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
readable Arabic signs, misspelled signage, brand logos, Gulf malls, skyscrapers, palm-lined boulevards, exoticized bazaar, belly dancers, hookah cliché focus
```

---

### 13A — المشهد 13: غزة والبحر

**Prompt**

```text
Cinematic documentary photograph, wide shot of the Mediterranean shoreline of Gaza at sunset: calm low waves rolling onto a long sandy beach, a few small brightly painted wooden fishing boats anchored offshore and two pulled up onto the sand, the silhouette of a fisherman standing knee-deep casting a net in the distance, dense concrete city buildings along the coast in soft haze. The sun low over the sea near the horizon, a warm orange-to-rose sky with thin clouds, reflections glittering on the wet sand. Eye level from the beach, 35mm prime lens, horizon on the lower third, boats on the right third, deep focus. Natural, restrained warm grade, not oversaturated, Kodak Vision3 250D emulation, subtle grain, photorealistic, peaceful and quietly melancholic, 16:9, no text, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
luxury yachts, resort beach, tourists in swimwear, sunbathers, warships, explosions, smoke columns, tropical palm resort, turquoise Caribbean water
```

---

### 13B — المشهد 13: غزة والبحر

**Prompt**

```text
Cinematic documentary portrait of a 55-year-old Palestinian fisherman from Gaza sitting on the edge of a small blue-and-white wooden boat at the fishing harbor, mending a green fishing net stretched across his knees, golden hour. Wiry strong build, deeply sun-darkened skin, salt-and-pepper stubble, short grey hair, crow's feet around kind tired eyes, a focused gentle expression; faded navy-blue long-sleeve cotton shirt with rolled sleeves, dark work trousers rolled at the ankles, plastic sandals. Background: other fishing boats, coiled ropes, floats and the harbor wall in soft focus, the sea glowing. Warm low sun from the side, a soft rim on his face and hands. Medium close-up at eye level, 50mm prime lens, shallow depth of field, subject on the left third. Natural skin texture with pores, salt and sun damage, realistic hands, restrained warm grade, subtle grain, photorealistic, dignified, 16:9, no text, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
luxury yachts, resort beach, tourists in swimwear, sunbathers, warships, explosions, smoke columns, tropical palm resort, turquoise Caribbean water
```

---

### 14A — المشهد 14: غزة والإنسان

**Prompt**

```text
Cinematic documentary photograph of a 36-year-old Palestinian mother in Gaza sitting on the doorstep of a modest concrete home with her two children in the late afternoon. She wears a dusty-rose headscarf and a long dark-grey coat-dress, has warm tired eyes and a soft genuine smile, and is braiding the hair of her 9-year-old daughter, who has a long dark-brown braid, olive skin and thoughtful dark eyes and wears a mustard-yellow knitted cardigan over a white t-shirt; a 5-year-old boy leans on his mother's shoulder holding a small toy car. A narrow sandy street, unplastered concrete walls, a potted plant, a water jerrycan; some distant damaged buildings softly blurred far in the background. Warm low sunlight from the right, soft shadows. Medium shot at seated eye level, 50mm prime lens, shallow depth of field, the family center-left. Natural, tender, unposed, realistic faces, natural skin texture, restrained warm grade, subtle grain, photorealistic, non-graphic, 16:9, no text, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
blood, injuries, bandages close-up, dead bodies, crying children close-up, explosions, smoke columns, aircraft, rubble as main subject, refugee stereotypes, begging gestures, pity framing, looking at camera pleading
```

---

### 14B — المشهد 14: غزة والإنسان

**Prompt**

```text
Cinematic documentary photograph of a Palestinian young man in his early twenties walking along a busy street in Gaza City in the late afternoon, carrying a stack of books under one arm and a small bag of bread in the other hand, seen from a slightly low three-quarter front angle. Short black hair, light beard, a focused calm expression; grey hoodie, dark jeans, worn sneakers. Around him: street vendors, a few cars and motorbikes, small shopfronts with blurred unreadable signs, concrete buildings with balconies, overhead tangles of electric wires. Warm hazy light with dust in the air. 35mm lens, moderate depth of field, the young man sharp and the background softly blurred. Authentic everyday street life, restrained grade, subtle grain, photorealistic, 16:9, no readable text, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
blood, injuries, bandages close-up, dead bodies, crying children close-up, explosions, smoke columns, aircraft, rubble as main subject, refugee stereotypes, begging gestures, pity framing, looking at camera pleading
```

---

### 14C — المشهد 14: غزة والإنسان

**Prompt**

```text
Cinematic documentary portrait of an elderly Palestinian man in his late seventies in Gaza, sitting on a plastic chair in front of a small shop at dusk, holding a string of prayer beads and looking calmly at the street. White stubble, a deeply lined face, kind patient eyes, a white knitted skullcap, a light-brown jacket over a white shirt. The last warm light on his face, soft shadows. Medium close-up, 85mm lens, shallow depth of field, background street lights and passing figures in soft bokeh. Natural skin texture, quiet dignity, restrained warm grade, subtle grain, photorealistic, 16:9, no text, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
blood, injuries, bandages close-up, dead bodies, crying children close-up, explosions, smoke columns, aircraft, rubble as main subject, refugee stereotypes, begging gestures, pity framing, looking at camera pleading
```

---

### 14D — المشهد 14: غزة والإنسان

**Prompt**

```text
Cinematic documentary photograph of a Palestinian vegetable vendor in his forties at a market stall in Gaza in the late afternoon, arranging tomatoes, cucumbers, eggplants and bunches of fresh mint and parsley on a wooden cart under a faded canvas shade; short dark hair, trimmed beard, a cheerful focused face; dark-green jacket over a t-shirt. A woman customer in a headscarf chooses produce in the slightly out-of-focus foreground. Warm side light filtering through the canvas, rich but natural colors. Medium shot, 35mm lens, moderate depth of field. Authentic everyday market, natural skin texture, restrained grade, subtle grain, photorealistic, 16:9, no readable text, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
blood, injuries, bandages close-up, dead bodies, crying children close-up, explosions, smoke columns, aircraft, rubble as main subject, refugee stereotypes, begging gestures, pity framing, looking at camera pleading
```

---

### 15A — المشهد 15: الأمل

**Prompt**

```text
Cinematic documentary photograph of a 9-year-old Palestinian girl from Gaza standing barefoot on the wet sand of the beach at sunset, seen in profile from slightly behind, looking toward the horizon over the sea. Slender, olive skin, dark-brown hair in a single long braid, thoughtful dark eyes, a calm expression with the faint beginning of a smile; a mustard-yellow knitted cardigan over a white t-shirt and dark-blue trousers. The warm low sun near the horizon creates a soft golden rim light around her hair and cardigan; gentle waves and a few distant fishing boats behind. Medium shot at her eye level, 85mm prime lens, very shallow depth of field, the girl on the left third with open space toward the sea, sea and sky in soft bokeh. Natural skin texture, restrained warm golden grade, not oversaturated, Kodak Vision3 250D emulation, subtle grain, photorealistic, hopeful and quiet, 16:9, no text, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
posed model, fashion editorial, glamour, makeup, staring into camera, sad crying face, oversaturated sunset, sun flare covering face, different clothing than reference
```

---

### 16A — المشهد 16: شجرة الزيتون

**Prompt**

```text
Cinematic documentary photograph of a very ancient Palestinian olive tree on a stone terrace at golden hour, framed from ground level at its base: enormous gnarled roots gripping red soil and limestone rocks, a massive twisted multi-stemmed trunk rising upward, young green shoots sprouting from the old base; a silver-green canopy above glowing in warm backlight against a clear sky turning amber. Terraced hills with more olive trees in the background. Extreme low angle, 24mm prime lens, deep focus, strong vertical composition. Rich bark and soil texture, warm restrained grade, gentle sun flare, Kodak Vision3 250D emulation, subtle grain, photorealistic, timeless and resilient, no people, 16:9, no text, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
fantasy tree, glowing magical light, tree of life illustration, giant oak, baobab, people, swing, dead tree
```

---

### 17A — المشهد 17: مونتاج الخاتمة

**Prompt**

```text
Cinematic documentary close-up of two hands at golden hour: the deeply lined, weathered hand of an 86-year-old Palestinian man, with a plain thin silver ring on the right ring finger and a charcoal-grey wool jacket cuff, gently placing an old hand-forged iron key with a large oval bow, long shaft and dark patina into the open small palm of a 10-year-old boy whose light-blue shirt cuff is visible. Background: an olive grove in warm backlight, soft bokeh. Side angle at hand level, 85mm lens, very shallow depth of field, the key in sharp focus centered between the hands. Natural skin textures, a clear contrast of old and young skin, warm restrained grade, Kodak Vision3 250D emulation, subtle grain, photorealistic, tender and solemn, 16:9, no text, no watermark.
```

**Negative** (NEG-IMAGE +)

```text
three hands, extra hands, different key shape, modern key, gloves, jewelry on child, fast flashy montage effects, glitch transitions
```
