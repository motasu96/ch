# جميع Prompts تحريك الصور (Image-to-Video) — مرتبة

> مُستخرجة آليًا من [`01_BLUEPRINT.md`](01_BLUEPRINT.md). لكل صورة في `03_IMAGE_PROMPTS.md` تحريك مقابل بالرمز نفسه.
> **الصور الأرشيفية (المشهدان 04 و06) لا تُحرَّك بالذكاء الاصطناعي إطلاقًا** — Ken Burns داخل المونتاج فقط.

## إعدادات عامة

| البند | الإعداد |
|---|---|
| الأدوات | Kling / Runway / Veo / Hailuo / Luma — **أداة واحدة لكل الفيلم** |
| المدة | 5–10 ث للتوليد؛ يُستخدم منها 3–7 ث فقط (أفضل جزء غالبًا في المنتصف) |
| Motion strength | منخفضة إلى متوسطة (مثلًا 3–5 من 10) |
| الدقة | 1080p على الأقل، ثم Upscale إلى 4K بحذر |
| Prompt | صف **الحركة فقط** — الصورة تتكفّل بالمظهر. لا تُعِد وصف المشهد كله. |

**قاعدة ذهبية:** إذا شوّهت الأداة وجهًا أو يدًا، خفّض قوة الحركة أو قصّر المدة أو استخدم Ken Burns على الصورة الثابتة بدلًا من التحريك. الصورة الثابتة الجيدة أفضل من فيديو مشوّه.

## Negative Prompt الموحّد للفيديو (NEG-VIDEO)

```text
warping faces, face morphing, identity drift, melting hands, extra fingers, deformed bodies, unnatural walking, sliding feet, floating objects, facial distortion, AI morphing, flicker, jitter, sudden zoom, fast camera movement, excessive camera shake, rubbery motion, objects appearing or disappearing, text appearing, warped buildings, bending architecture, exaggerated expressions, unnatural slow motion
```

---

### 01A — المشهد 01: الفجر

```text
Very slow forward dolly push-in toward the village across the valley, about 5 percent total scale change, perfectly steady gimbal motion. Low mist drifts slowly to the left along the valley floor; olive leaves in the foreground tremble gently in a light breeze; a few small birds cross the sky far away; the sky brightens almost imperceptibly toward warm apricot. Buildings stay completely rigid and geometrically stable. No people, no new objects appearing, no warping of architecture, no flicker. Realistic real-time speed, cinematic documentary feel, 10 seconds.
```

---

### 02A — المشهد 02: التراب والزيتون

```text
Locked-off macro shot with an extremely slow push-in. The old man's fingers close slowly and gently around the soil; a few fine grains of soil trickle down between the fingers and fall naturally with gravity; subtle breath-like micro movement in the hands. The background bokeh shimmers softly as olive leaves move in the breeze. Each hand keeps exactly five fingers, anatomy stays stable, the silver ring stays on the same finger, no morphing, no melting. 6 seconds, real-time speed.
```

---

### 02B — المشهد 02: التراب والزيتون

```text
Slow, smooth vertical tilt-up from the twisted lower trunk to the silver-green canopy, combined with a very slight forward drift. Leaves and thin branches sway softly in a natural light wind; sunlight flickers gently through the canopy; a faint flare breathes in and out. The trunk keeps its exact shape, solid and stable, no bending or morphing of the bark. 6 seconds.
```

---

### 03A — المشهد 03: إيقاع الحياة

```text
Subtle handheld documentary motion, almost static. The grandmother lifts the bread slowly, turns it over with a natural practiced hand movement and places it on the wooden board; thin smoke rises and curls through the sunbeam; the edge of her headscarf moves slightly; natural blinking and breathing. Hands stay anatomically correct with five fingers, face identity stays stable, the embroidery pattern does not change. 6 seconds, real-time.
```

---

### 03B — المشهد 03: إيقاع الحياة

```text
Slow lateral dolly to the left at walking pace. The farmer completes one natural, unhurried hoe stroke into the soil; small clods of earth break apart and a little dust lifts; his jacket fabric moves with his body; olive leaves shimmer in the breeze. Natural human motion with correct weight and timing, no limb distortion, consistent face. 6 seconds.
```

---

### 03C — المشهد 03: إيقاع الحياة

```text
Static camera with subtle handheld breathing. The children run down the steps toward and past the camera with a natural gait and realistic foot placement; light shifts across them as they pass through the sunbeams; grapevine leaves sway gently overhead. Correct anatomy, exactly three children, no duplicated children, no merging limbs, no floating. 5 seconds, real-time.
```

---

### 07A — المشهد 07: الطريق (مشهد تمثيلي)

```text
The camera follows slowly from behind at ground level as the feet walk away along the dusty road with natural, tired, unhurried steps; fine dust rises and drifts; the cloth bundle sways with each step; the child's steps are shorter and quicker than the adults'. Natural gait, correct number of feet and legs, feet grounded, no sliding or floating. 6 seconds.
```

---

### 07B — المشهد 07: الطريق (مشهد تمثيلي)

```text
Locked-off wide shot with an extremely slow push-in. The small figures walk slowly away along the road at a natural, consistent pace; low clouds drift slowly; dry grass moves in a cold wind; the light dims very slightly. The figure count stays exactly five, no merging, no duplication, no sliding. 6 seconds.
```

---

### 08A — المشهد 08: المفتاح

```text
Very slow orbital arc of about 15 degrees around the key from left to right, with a gentle focus pull traveling from the key's bit to its oval bow. The old man's fingers close slightly around the key with a tiny natural tremor of age; dust particles drift through the window beam. The key's shape stays absolutely rigid and consistent, hand anatomy stable, the ring stays on the same finger, no morphing. 7 seconds.
```

---

### 08B — المشهد 08: المفتاح

```text
Extremely slow push-in on the face. The old man breathes slowly; his eyes blink naturally once and then shift subtly from the window down toward the key in his hands; a very slight movement of the lips as if about to speak, but he stays silent. Dust floats in the window light. Face identity, beard shape and wrinkles remain consistent, no facial morphing, no exaggerated emotion. 7 seconds.
```

---

### 09A — المشهد 09: الذاكرة

```text
Static camera with a very subtle handheld drift. The hand turns one album page slowly and naturally; the page bends with realistic paper physics and settles flat; a faint shadow passes across the photographs; the tea surface trembles slightly. Five fingers, stable anatomy, the photographs stay blurred and never morph into faces. 5 seconds.
```

---

### 09B — المشهد 09: الذاكرة

```text
Slow dolly forward past the out-of-focus cactus pads toward the standing arch, revealing it gradually; wild grass moves in a light wind; clouds drift slowly overhead. The stones and the arch remain rigid and stable, no warping. 5 seconds.
```

---

### 10A — المشهد 10: الأجيال الجديدة

```text
Smooth, slow tracking shot moving backward at the boy's walking pace with slight natural handheld sway. He walks with a relaxed natural gait, adjusts his backpack strap once, and glances briefly toward the sun; his hair and shirt move lightly; olive leaves sway at the roadside. Realistic walking cycle, feet grounded, no sliding, consistent face. 6 seconds.
```

---

### 10B — المشهد 10: الأجيال الجديدة

```text
Subtle handheld documentary motion with a slow drift to the right. The students move naturally: a few hands go up, one boy turns his head to whisper and smile, pages turn, light dust floats in the window light. No warping faces, no duplicated children, consistent desk geometry. 5 seconds.
```

---

### 11A — المشهد 11: الزيتون

```text
Slow gentle pedestal-down from canopy level to the family on the ground with a slight forward drift. The farmer's hands strip olives from a branch, the olives fall naturally and bounce on the tarp; the women and the boy gather olives with natural movements; leaves flutter in the breeze. Correct anatomy, consistent faces, no floating olives. 7 seconds.
```

---

### 11B — المشهد 11: الزيتون

```text
Locked-off shot with a very slow push-in. A few olives roll naturally within the cupped hands and one drops to the tarp below; backlit leaves tremble in the breeze. Five fingers on each hand, olives keep their shape, no morphing. 5 seconds.
```

---

### 12A — المشهد 12: المدينة

```text
Subtle handheld documentary motion with a slow push forward through the crowd. People walk naturally in different directions at believable speeds, the cart rolls forward, a shopkeeper hands a bag to a customer; sunlit dust is visible under the arch. No sliding feet, no merging people, stable faces, the arches remain rigid. 5 seconds.
```

---

### 12B — المشهد 12: المدينة

```text
Gentle slow lateral slide. Natural conversation: one young man laughs, a woman sips her coffee and puts the cup down, another turns to listen; a car passes softly out of focus in the background. Natural lip and eye movement, no facial distortion, cups keep their shape. 5 seconds.
```

---

### 12C — المشهد 12: المدينة

```text
Very slow pan from left to right across the rooftops; pigeons circle naturally; laundry moves in the breeze; the sunlight warms subtly. Buildings remain completely rigid, no warping. 6 seconds.
```

---

### 13A — المشهد 13: غزة والبحر

```text
Locked-off wide shot with a very slow push-in toward the sea. Gentle waves roll in and recede naturally with realistic foam; anchored boats rock slowly; the distant fisherman's net opens and falls; seagulls glide across; sunlight glitters on the water. The horizon stays level and stable, no warping of buildings. 7 seconds.
```

---

### 13B — المشهد 13: غزة والبحر

```text
Subtle handheld documentary motion, nearly static. The fisherman's hands work the net with a wooden netting needle in slow, practiced movements, pulling a knot tight; he breathes and blinks naturally and glances once toward the sea; the boat rocks very slightly; water reflections dance on the hull. Hands anatomically correct, net pattern consistent, face identity stable. 6 seconds.
```

---

### 14A — المشهد 14: غزة والإنسان

```text
Static camera with subtle handheld breathing. The mother's fingers continue braiding her daughter's hair with natural, careful motion; the daughter blinks and smiles slightly; the little boy shifts his weight and rolls the toy car along his mother's arm. Natural breathing, consistent faces, correct hands, no morphing. 6 seconds.
```

---

### 14B — المشهد 14: غزة والإنسان

```text
Slow backward tracking shot at walking pace with natural handheld sway. The young man walks with a natural gait and glances to the side at a passing motorbike; background people move naturally; dust drifts in the light. Feet grounded, no sliding, consistent face, the books keep their shape. 5 seconds.
```

---

### 14C — المشهد 14: غزة والإنسان

```text
Extremely slow push-in. The man passes the beads slowly between his fingers, breathes, blinks, and gives a small gentle nod to someone off-camera. Face and hands stable, no morphing. 5 seconds.
```

---

### 14D — المشهد 14: غزة والإنسان

```text
Subtle handheld motion. The vendor places a tomato on the pile and hands a small bunch of mint to the customer with a smile; the canvas shade moves slightly in the breeze; natural crowd movement in the background. Correct hands, consistent produce, no morphing. 5 seconds.
```

---

### 15A — المشهد 15: الأمل

```text
Very slow push-in with a slight arc toward her face. The sea breeze moves stray hairs and the edge of the cardigan; she breathes calmly, blinks, and slowly lifts her chin a little toward the horizon; waves glisten in the background bokeh. Face identity stable, braid consistent, no facial distortion. 7 seconds.
```

---

### 16A — المشهد 16: شجرة الزيتون

```text
Slow continuous vertical crane and tilt-up starting at the roots and young shoots, rising along the twisted trunk to the glowing canopy and the open sky, ending on soft sun flare through the leaves. Leaves move in a light breeze, light rays flicker naturally. The trunk geometry stays stable, no morphing bark. 8 seconds.
```

---

### 17A — المشهد 17: مونتاج الخاتمة

```text
Locked-off shot with a very slow push-in. The old hand lowers the key slowly into the boy's palm and lingers for a moment; the boy's fingers close gently around the key; leaves shimmer in the background bokeh. Exactly two hands, five fingers each, the key's shape identical to the reference, no morphing. 6 seconds.
```
