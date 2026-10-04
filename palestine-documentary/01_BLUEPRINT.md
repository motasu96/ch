# «فلسطين: حكاية أرض وذاكرة»
## المخطط الإنتاجي الكامل (Production Blueprint)

| | |
|---|---|
| **النوع** | فيلم وثائقي سينمائي قصير |
| **المدة** | 3:10 دقيقة (190 ثانية) |
| **اللغة** | العربية الفصحى + ترجمة إنجليزية (Subtitles) |
| **الجمهور** | عربي وعالمي |
| **نسبة العرض** | 16:9 — 3840×2160 — 24fps |
| **عدد المشاهد** | 18 مشهدًا في 6 فصول |
| **الأسلوب** | Cinematic documentary — إنساني، هادئ، غير دعائي |

**الفكرة في جملة (Logline):**
من فجر قرية فلسطينية إلى غروب على شاطئ غزة، يتتبّع الفيلم خيطًا واحدًا — الأرض، والبيت، والمفتاح، وشجرة الزيتون — ليروي كيف تحوّلت حكاية مكانٍ إلى ذاكرةِ شعبٍ كامل، وكيف ما زالت هذه الذاكرة تُورَّث من جيل إلى جيل.

**الخيط الدرامي:** عائلة تمثيلية واحدة عبر ثلاثة أجيال:
**أبو خليل** (86 عامًا، وُلد قبل 1948) ← ابنه **أحمد** (مزارع) ← حفيده **يوسف** (10 أعوام).
في غزة: الصيّاد **أبو سمير**، والطفلة **ليلى** ووالدتها.
المفتاح الحديدي ينتقل في النهاية من يد الجدّ إلى يد الحفيد.

> **مبدأ أساسي:** كل ما هو تاريخي يأتي من **أرشيف حقيقي**. كل ما هو مولَّد بالذكاء الاصطناعي هو **مشهد تمثيلي معاصر أو رمزي**، ويُفصَح عنه في الشارة الختامية. لا نولّد صورًا "تاريخية" مزيّفة، ولا نحرّك صور اللاجئين الأرشيفية بالذكاء الاصطناعي.

---

## الفهرس

1. [الهوية البصرية](#أولًا-الهوية-البصرية)
2. [قواعد الاستمرارية + دليل الشخصيات والأماكن](#ثانيًا-قواعد-الاستمرارية)
3. [البنية الدرامية](#ثالثًا-البنية-الدرامية)
4. [الـ Negative Prompt الموحّد](#رابعًا-negative-prompt-الموحد)
5. [المشاهد 1–18 بالتفصيل](#خامسًا-المشاهد-بالتفصيل)
6. [الجدول المختصر](#سادسًا-الجدول-المختصر)
7. [ملفات المخرجات النهائية](#سابعًا-المخرجات-النهائية)
8. [سياسة الشفافية والأخلاقيات](#ثامنًا-سياسة-الشفافية-والأخلاقيات)

---

## أولًا: الهوية البصرية

### اسم الـ Look: «ضوء الحجر» (Limestone Light)
فيلم يبدو كأنه صُوِّر بكاميرا واحدة، بطاقم واحد، في رحلة واحدة عبر فلسطين.

### الكاميرا والعدسات (الحزمة الافتراضية الثابتة)
| العنصر | المواصفة | الاستخدام |
|---|---|---|
| الكاميرا | ARRI Alexa Mini LF look | كل اللقطات المولّدة |
| 24mm prime | Ultra-wide | لقطة واحدة فقط: جذور الزيتونة (م16) |
| **35mm prime** | **العدسة الرئيسية** | اللقطات الواسعة والمتوسطة والبيئة |
| 50mm prime | Medium | لقطات الأشخاص والتفاعل |
| 85mm prime | Portrait | البورتريهات العاطفية (أبو خليل، ليلى) |
| 100mm macro | Macro | التراب، المفتاح، الزيتون، الأيدي |

- Shutter 180° (Motion blur طبيعي) — 24fps — نسبة 16:9 دائمًا.
- لا عدسات Fisheye، لا Anamorphic flares ملوّنة، لا Tilt-shift.

### لوحة الألوان (Color Tokens)
| الاسم | HEX | الاستخدام |
|---|---|---|
| Limestone | `#CDBFA3` | الحجر، الإضاءات العالية الدافئة |
| Olive | `#6B7550` | الأخضر المكتوم للنبات |
| Terra Rossa | `#7A4A35` | تربة فلسطين الحمراء |
| Tatreez Red (مكتوم) | `#8A2E2A` | لمسات نادرة: التطريز، فواصل النصوص «•» |
| Sea Dusk | `#4E6A72` | بحر غزة عند الغروب |
| Off-White | `#EDE8DF` | الطباعة على الشاشة |
| Charcoal | `#0E0E0E` | الخلفيات الداكنة والشاشة الختامية |

### التلوين (Grade) — ثابت لكل الفيلم
- Film emulation: **Kodak Vision3 250D** للنهار، **500T** للداخلي، مع print emulation **Kodak 2383** خفيف.
- Saturation عام 85–90%، الأخضر مكتوم نحو الزيتي، البشرة على خط الـ Skin tone line.
- Blacks مرفوعة قليلًا (~3%)، Highlights roll-off ناعم، بلا HDR halos.
- **Grain:** طبقة 35mm grain واحدة على كل اللقطات المولّدة بشفافية 8–12% (نفس الملف، نفس الإعداد).
- الصور الأرشيفية تحتفظ بحبيباتها الأصلية — **لا تُلوَّن ولا يُضاف لها grain ثقيل**.

### قوس الضوء عبر الفصول (Light Arc)
| الفصل | الضوء | الحرارة اللونية | الإحساس |
|---|---|---|---|
| 1 — الأرض والذاكرة | فجر، ضوء غير مباشر ثم شمس منخفضة | دافئ ناعم | سكينة |
| 2 — الحياة قبل التحوّل | صباح مشمس ← أرشيف بالأبيض والأسود/السيبيا | دافئ ← محايد | ألفة |
| 3 — النكبة والذاكرة | غيوم، ضوء منتشر بارد ← ضوء نافذة داخلي دافئ | بارد ← دافئ خافت | فقد، ثم حنين |
| 4 — الحياة المعاصرة | صباح وضحى، ضوء طبيعي | محايد مائل للدفء | حياة |
| 5 — غزة | الساعة الذهبية والغروب | دافئ ذهبي مع ظلال زرقاء | كرامة وصبر |
| 6 — الهوية والأمل | ذهبي ← غسق ← ظلام الشاشة الختامية | ذهبي ← أسود | أمل هادئ |

### Style Anchor (الجملة الأسلوبية المرجعية)
تُستخدم روحها — لا نصّها الحرفي — في كل Prompt:
> *cinematic documentary photograph, authentic Palestinian environment, natural light, shot on ARRI Alexa Mini LF, [lens], Kodak Vision3 film emulation, subtle 35mm film grain, restrained warm-neutral grade with muted olive greens and limestone highlights, natural skin texture, photorealistic, emotionally restrained, 16:9, no text, no watermark.*

### ما نتجنّبه بصريًا
plastic skin · AI-looking faces · overly perfect faces · fantasy elements · excessive HDR · oversaturated colors · cartoon · anime · 3D render · video game look · fake historical costumes · text inside images · watermarks · logos
**+ إضافات خاصة بالمشروع:** كثبان رملية وجِمال (ليست بيئة فلسطين الريفية)، عمارة خليجية أو مغاربية، أعلام وملصقات سياسية في الصور المولّدة، أسلحة وجنود ودماء، الكوفية على رأس كل رجل (صورة نمطية)، إضاءة "إعلانية" أو Beauty filter.

---

## ثانيًا: قواعد الاستمرارية

| # | العنصر | القاعدة |
|---|---|---|
| 1 | الإضاءة | ضوء طبيعي دائمًا ومُبرَّر (شمس، نافذة، سماء). لا إضاءة استوديو. اتبع «قوس الضوء» أعلاه. |
| 2 | العدسات | 35mm رئيسية؛ 50/85 للأشخاص؛ 100mm macro للتفاصيل. لا تغيّر العدسة داخل المشهد الواحد إلا لسبب. |
| 3 | الألوان | نفس الـ LUT ونفس طبقة الـ Grain على كل اللقطات المولّدة. |
| 4 | البيئة | حجر جيري كريمي/عسلي، مدرّجات بجدران حجرية جافة (سناسل)، زيتون، لوز، صبّار، خزانات مياه سوداء وسخّانات شمسية على الأسطح (في المشاهد المعاصرة). |
| 5 | الملابس | ثابتة لكل شخصية (انظر الدليل). |
| 6 | الشخصيات | نفس الوصف الإنجليزي الحرفي في كل Prompt + صور مرجعية (Character reference). |
| 7 | الأسلوب | Documentary observational: لا لقطات "بطولية" ولا Slow-motion استعراضي. |
| 8 | الواقعية | كل وجه يحمل مسام وتجاعيد وعدم تماثل طبيعي. |
| 9 | حركة الكاميرا | بطيئة ومُبرَّرة: Push-in، Dolly، Tilt، Handheld خفيف فقط في المدينة وغزة. |
| 10 | النسبة | 16:9 في كل توليد (`--ar 16:9` أو ما يعادله). |

### دليل الشخصيات (Character Bible)
> انسخ **الوصف الإنجليزي المقفل** حرفيًا في كل Prompt تظهر فيه الشخصية. جميع الشخصيات **تمثيلية مركّبة** وليست أشخاصًا حقيقيين.

**C1 — أبو خليل (الجدّ، 86 عامًا)** — المشاهد: 2A، 8A، 8B، 9A، 17A
> *an 86-year-old Palestinian man, lean build, deeply lined sun-weathered olive-brown skin, short neatly trimmed white beard, thin white hair, warm dark-brown eyes with slight age clouding, large knotted hands with visible veins and age spots, a plain thin silver ring on the right ring finger, white-and-black checkered keffiyeh draped loosely over his shoulders (not on his head), charcoal-grey wool jacket over a faded beige collarless shirt, dark trousers*

علامة الاستمرارية الحاسمة: **الخاتم الفضي** في البنصر الأيمن + **كمّ الجاكيت الرمادي الفحمي** — هما ما يربط لقطات الأيدي ببعضها.

**C2 — أحمد (الابن، مزارع، 46 عامًا)** — المشاهد: 3B، 11A، 11B
> *a 46-year-old Palestinian farmer, medium-stocky build, sun-tanned skin, short black hair greying at the temples, short dark beard with grey streaks, calm focused expression, faded olive-green work jacket over a blue-grey checkered flannel shirt, worn jeans, dusty brown work boots*

**C3 — يوسف (الحفيد، 10 أعوام)** — المشاهد: 3C، 10A، 10B، 11A، 17A
> *a 10-year-old Palestinian boy, slim, light olive skin, short dark-brown wavy hair, large dark eyes, curious alert expression, light-blue collared shirt, navy-blue trousers, scuffed white sneakers, worn dark-blue backpack with one frayed strap*

**C4 — الحاجّة آمنة (الجدّة، 80 عامًا)** — المشاهد: 3A، (17 مونتاج)
> *an 80-year-old Palestinian grandmother, round kind face, deep wrinkles, soft brown eyes, loose white cotton headscarf, traditional black thobe with deep-red cross-stitch tatreez embroidery on the chest panel, sleeves pushed to the forearms*

ملاحظة: أنماط التطريز تختلف حسب المنطقة؛ اختر نمطًا واحدًا وثبّته (مثلًا الأحمر العميق على الأسود — شائع في الوسط والجنوب) ولا تخلط الأنماط.

**C5 — أبو سمير (صيّاد من غزة، 55 عامًا)** — المشاهد: 13A (ظل بعيد)، 13B، (17)
> *a 55-year-old Palestinian fisherman from Gaza, wiry strong build, deeply sun-darkened skin, salt-and-pepper stubble, short grey hair, crow's feet around kind tired eyes, faded navy-blue long-sleeve cotton shirt with rolled sleeves, dark work trousers rolled at the ankles, plastic sandals*

**C6 — ليلى (طفلة من غزة، 9 أعوام)** — المشاهد: 14A، 15A، (17)
> *a 9-year-old Palestinian girl from Gaza, slender, olive skin, dark-brown hair in a single long braid, thoughtful dark eyes, mustard-yellow knitted cardigan over a white t-shirt, dark-blue trousers*

**C7 — أم ليلى (36 عامًا)** — المشهد: 14A
> *a 36-year-old Palestinian mother, warm tired eyes, makeup-free face, dusty-rose headscarf, long dark-grey coat-dress*

### دليل الأماكن (Location Bible)
| الرمز | المكان | العناصر الثابتة |
|---|---|---|
| L1 | قرية في المرتفعات الوسطى (الضفة الغربية) | مدرّجات وسناسل، زيتون عتيق، بيوت حجر جيري بأقواس، مئذنة متواضعة، خزانات مياه سوداء. مرجع بصري: مشهد بتّير الثقافي (موقع تراث عالمي، اليونسكو 2014). |
| L2 | بيت أبو خليل (داخلي) | جدران مطلية بالأبيض، نافذة خشبية، خزانة خشبية قديمة، ضوء عصر جانبي من اليسار. |
| L3 | مدينة في الضفة (نابلس/رام الله/بيت لحم) | أسواق حجرية مقبّبة، كنافة، أسطح مزدحمة بالخزانات والسخانات الشمسية، مآذن وأبراج كنائس. |
| L4 | غزة — الساحل والميناء | رمل، قوارب صيد خشبية ملوّنة، شباك خضراء، مبانٍ خرسانية كثيفة على الساحل، أسلاك كهرباء متشابكة. |

### سير العمل لضمان الاتساق (Consistency Workflow)
1. **ولّد Character Sheet لكل شخصية أولًا** (وجه أمامي، جانبي، ¾، يدان) واعتمد صورة واحدة كمرجع رسمي.
2. استخدم ميزة المرجع في أداتك: Midjourney `--oref`/`--cref` + `--ow`، أو Flux Kontext، أو Ideogram Character، أو Runway References، أو Kling Elements.
3. **أداة توليد صور واحدة وأداة فيديو واحدة لكامل الفيلم** — خلط الأدوات يغيّر "الفيلم".
4. ولّد لقطات كل شخصية دفعة واحدة، واحفظ الـ Seed لكل لقطة معتمدة.
5. أضف الـ LUT نفسه وطبقة الـ Grain نفسها في المونتاج لتوحيد ما تبقّى من اختلافات.
6. للصور المولّدة التي تحتاج حركة Tilt عمودية طويلة (م2B، م16): ولّد نسخة طولية إضافية واصنع الحركة بـ Pan داخل المونتاج كخطة بديلة مضمونة.

---

## ثالثًا: البنية الدرامية

| الفصل | المشاهد | الزمن | المحتوى | منحنى الشعور |
|---|---|---|---|---|
| 1 — الأرض والذاكرة | 1–2 | 0:00–0:24 | الفجر، التراب، الزيتون | سكينة |
| 2 — فلسطين قبل التحوّل | 3–5 | 0:24–0:53 | حياة القرية، أرشيف المدن، الخريطة | ألفة ← ترقّب |
| 3 — النكبة والذاكرة | 6–9 | 0:53–1:39 | 1948، الطريق، المفتاح، الألبوم | فقد ← حنين |
| 4 — الحياة المعاصرة | 10–12 | 1:39–2:07 | المدرسة، الزيتون، المدينة | حياة |
| 5 — غزة والإنسان | 13–14 | 2:07–2:33 | البحر، الصيّاد، الناس | كرامة وصبر |
| 6 — الهوية والأمل | 15–18 | 2:33–3:10 | الطفلة والأفق، الزيتونة، المونتاج، العنوان | أمل هادئ |

```
الشدة العاطفية
  ▲
  │                                                      ╭──╮ ذروة م17
  │                     ╭───╮                        ╭──╯  │
  │                ╭────╯   ╰──╮               ╭────╯      │
  │          ╭─────╯           ╰──╮       ╭───╯            ╰─ صمت ← «فلسطين»
  │ ╭────────╯                    ╰───────╯
  └─┴──────┴──────────┴───────────────┴──────────┴──────────┴──────▶ الزمن
    ف1     ف2         ف3 (النكبة)      ف4         ف5 (غزة)    ف6
```

---

## رابعًا: Negative Prompt الموحّد

### NEG-IMAGE (لكل الصور)
```text
cartoon, anime, illustration, 3D render, CGI, video game graphics, plastic skin, artificial face, deformed face, distorted anatomy, extra fingers, missing fingers, malformed hands, duplicated people, duplicated objects, unnatural eyes, asymmetrical face, unrealistic skin, oversaturated colors, excessive HDR, fantasy architecture, generic Middle Eastern stereotypes, fake historical costumes, text, subtitles, captions, logo, watermark, blurry face, low resolution, excessive sharpening, unrealistic motion, melting objects, warped buildings, distorted background, airbrushed skin, beauty filter, glamour lighting, studio lighting, desert dunes, camels, Gulf-style architecture, Moroccan architecture, flags, political posters, graffiti slogans, weapons, soldiers, blood, injuries
```

### NEG-VIDEO (لكل تحريك)
```text
warping faces, face morphing, identity drift, melting hands, extra fingers, deformed bodies, unnatural walking, sliding feet, floating objects, facial distortion, AI morphing, flicker, jitter, sudden zoom, fast camera movement, excessive camera shake, rubbery motion, objects appearing or disappearing, text appearing, warped buildings, bending architecture, exaggerated expressions, unnatural slow motion
```

في كل مشهد أدناه: **NEG = NEG-IMAGE + الإضافات الخاصة بالمشهد**.

---

## خامسًا: المشاهد بالتفصيل

---

### المشهد 01 — الفجر
**الفصل الأول: الأرض والذاكرة**

**SCENE NUMBER:** 01

**TIME CODE:** 00:00 – 00:13

**DURATION:** 13 ثانية (لقطة واحدة طويلة)

**PURPOSE OF THE SCENE:** افتتاح هادئ جدًا يضع المشاهد في المكان قبل أي معلومة. الصمت والضوء والأرض أولًا. يطرح الفكرة المركزية: فلسطين مكان يسكن الذاكرة.

**VISUAL DESCRIPTION:** لقطة واسعة جدًا لقرية فلسطينية على تلّة مدرّجة قبل شروق الشمس بدقائق. بيوت حجرية متدرّجة على المنحدر، مئذنة متواضعة، أشجار زيتون عتيقة في المقدّمة، ضباب خفيف يستقر في الوادي، نافذة واحدة مضاءة. لا بشر.

**CAMERA ANGLE:** مستوى العين، من تلّة مقابلة.

**CAMERA MOVEMENT:** Slow cinematic push-in شبه غير محسوس (~5% تكبير على 13 ثانية).

**LENS:** 35mm prime.

**LIGHTING:** ضوء سماء الفجر غير المباشر، تدرّج من الأزرق الباهت إلى المشمشي، حافة دافئة على خط التلال.

**ENVIRONMENT:** L1 — مدرّجات، سناسل، زيتون، بيوت جيرية، خزانات مياه سوداء على بعض الأسطح.

**CHARACTER DESCRIPTION:** لا شخصيات.

**CHARACTER CONSISTENCY NOTES:** — (تُثبَّت هنا هوية القرية L1 التي ستعود في م3، م10، م11).

**IMAGE GENERATION PROMPT — 01A**
<!-- IMG 01A -->
```text
Cinematic documentary photograph, extreme wide establishing shot of a quiet Palestinian hill village in the central West Bank highlands at first light, about ten minutes before sunrise. Clusters of old cream-and-honey limestone houses with arched windows, flat roofs and a few small domes stacked along a terraced hillside; dry-stone terrace walls lined with ancient gnarled olive trees in the foreground; a modest stone minaret rising among the roofs; a few black rooftop water tanks; a single warm window light still on. Weather: clear and still, thin layers of low morning mist resting in the valley, pale blue-to-apricot sky gradient, no visible sun disc yet. Lighting: soft indirect dawn skylight, a gentle warm rim along the ridge line, deep but readable shadows. Camera at eye level from the opposite hillside, 35mm cinema prime on ARRI Alexa Mini LF, rule-of-thirds composition with the village on the right third and olive branches framing the lower-left foreground, deep focus with natural atmospheric falloff. No people. Restrained documentary color grade, muted olive greens, warm limestone highlights, slightly lifted shadows, Kodak Vision3 250D film emulation, subtle 35mm film grain, natural high dynamic range without halos, photorealistic, authentic Palestinian architecture, serene and contemplative, 16:9, no text, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 01A**
<!-- I2V 01A -->
```text
Very slow forward dolly push-in toward the village across the valley, about 5 percent total scale change, perfectly steady gimbal motion. Low mist drifts slowly to the left along the valley floor; olive leaves in the foreground tremble gently in a light breeze; a few small birds cross the sky far away; the sky brightens almost imperceptibly toward warm apricot. Buildings stay completely rigid and geometrically stable. No people, no new objects appearing, no warping of architecture, no flicker. Realistic real-time speed, cinematic documentary feel, 10 seconds.
```

**MOTION GRAPHICS:** MG-01 — العنوان الرئيسي يظهر من 00:08 إلى 00:13: «فلسطين» ثم تحتها «حكاية أرض وذاكرة» (Fade-in 18 فريم + انجراف عمودي 8px). يختفي مع نهاية اللقطة.

**VOICE OVER:** (يبدأ عند 00:02)
> هناكَ أماكنُ لا تُختصَرُ في خطوطٍ على خريطة...
> أماكنُ تسكنُنا، قبلَ أن نسكنَها.
> وفلسطينُ... واحدةٌ من تلك الأماكن.

**SOUND EFFECTS:** رياح فجر خفيفة جدًا، ديك بعيد واحد، زقزقة طيور متفرّقة تتزايد ببطء، صدى خافت لوادٍ.

**MUSIC:** Cue M1 «فجر» — Drone منخفض على نغمة D، Pad هوائي، بلا إيقاع.

**TRANSITION TO NEXT SCENE:** Slow cross-dissolve (24 فريم) من القرية إلى اليد والتراب.

**NEGATIVE PROMPT:** NEG-IMAGE + `people, cars, modern high-rise buildings, sun disc, lens flare, fog too dense, snow`

---

### المشهد 02 — التراب والزيتون
**الفصل الأول: الأرض والذاكرة**

**SCENE NUMBER:** 02

**TIME CODE:** 00:13 – 00:24

**DURATION:** 11 ثانية (2A: 5 ث — 2B: 6 ث)

**PURPOSE OF THE SCENE:** تحويل "الأرض" من مفهوم إلى ملمس: يد، تراب، جذع. تقديم أبو خليل عبر يديه فقط — وجهه يُحفَظ للمشهد 8.

**VISUAL DESCRIPTION:** 2A: Macro ليدين مسنّتين تمسكان حفنة من التربة الحمراء، حبيبات تتسرّب بين الأصابع، الخاتم الفضي ظاهر. 2B: جذع زيتونة عتيقة ملتوٍ ومجوّف، والكاميرا تصعد نحو الأغصان.

**CAMERA ANGLE:** 2A: من أعلى بزاوية 30°. 2B: زاوية منخفضة من قاعدة الجذع.

**CAMERA MOVEMENT:** 2A: Locked-off مع Push-in بالغ البطء. 2B: Tilt-up سلس من الجذع إلى الأغصان.

**LENS:** 2A: 100mm macro. 2B: 35mm prime.

**LIGHTING:** بعد الشروق مباشرة؛ ضوء جانبي دافئ منخفض يكشف ملمس الجلد والتراب.

**ENVIRONMENT:** L1 — كرم زيتون مدرّج، تربة حمراء (Terra rossa)، حجارة، عشب جاف.

**CHARACTER DESCRIPTION:** أبو خليل (C1) — يداه فقط.

**CHARACTER CONSISTENCY NOTES:** الخاتم الفضي في البنصر الأيمن، كمّ الجاكيت الرمادي الفحمي، القميص البيج. نفس اليدين ستعودان في 8A و9A و17A.

**IMAGE GENERATION PROMPT — 02A**
<!-- IMG 02A -->
```text
Cinematic documentary macro photograph of the weathered hands of an 86-year-old Palestinian man scooping and loosely holding a handful of dark red-brown terra rossa soil in an olive grove. Large knotted fingers, prominent veins, age spots, deep creases filled with fine soil, short clean nails, a plain thin silver ring on the right ring finger; the cuff of a charcoal-grey wool jacket and a faded beige shirt sleeve visible at the frame edge. Location: a terraced olive grove in the Palestinian central highlands, early morning just after sunrise, clear weather. Lighting: low warm side light from the left raking across the skin and soil grains, soft natural fill, gentle glow in the background. Shot with a 100mm macro lens on ARRI Alexa Mini LF, camera slightly above at a 30-degree angle, hands centered in the lower two-thirds of the frame, very shallow depth of field with the background dissolving into soft olive-green and gold bokeh. Natural skin texture with pores and fine wrinkles, tactile and intimate, restrained documentary color grade, Kodak Vision3 250D emulation, subtle 35mm grain, photorealistic, no CGI, 16:9, no text, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 02A**
<!-- I2V 02A -->
```text
Locked-off macro shot with an extremely slow push-in. The old man's fingers close slowly and gently around the soil; a few fine grains of soil trickle down between the fingers and fall naturally with gravity; subtle breath-like micro movement in the hands. The background bokeh shimmers softly as olive leaves move in the breeze. Each hand keeps exactly five fingers, anatomy stays stable, the silver ring stays on the same finger, no morphing, no melting. 6 seconds, real-time speed.
```

**IMAGE GENERATION PROMPT — 02B**
<!-- IMG 02B -->
```text
Cinematic documentary photograph of a single ancient Palestinian olive tree with a massive, hollowed, twisted trunk split into several sculptural sections and a silver-green canopy above, standing on a stone terrace in an olive grove in the hills near Bethlehem, morning sunlight. Low-angle medium-wide shot from near the base, 35mm prime lens, the trunk filling the left two-thirds of the frame, the canopy cut by the top edge, soft sun flare filtering through leaves at the upper right. Reddish soil, dry grass and scattered limestone rocks around the roots, a dry-stone terrace wall behind. Clear sky with light haze. Natural warm morning light, deeply textured bark, moderate depth of field with the background grove gently out of focus. Restrained grade with muted silvery greens and warm earth tones, Kodak Vision3 250D emulation, fine film grain, natural dynamic range, photorealistic, timeless and dignified, no people, 16:9, no text, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 02B**
<!-- I2V 02B -->
```text
Slow, smooth vertical tilt-up from the twisted lower trunk to the silver-green canopy, combined with a very slight forward drift. Leaves and thin branches sway softly in a natural light wind; sunlight flickers gently through the canopy; a faint flare breathes in and out. The trunk keeps its exact shape, solid and stable, no bending or morphing of the bark. 6 seconds.
```

**MOTION GRAPHICS:** MG-02 (اختياري) — علامة فصل صغيرة «الأرض» أسفل يمين الكادر عند 00:15 لمدة ثانيتين.

**VOICE OVER:** (يبدأ عند 00:14)
> هنا، لم تكنِ الأرضُ مكانًا للعيشِ فحسب...
> كانت بيتًا، وذاكرةً، واسمًا يرثُه الأبناءُ عن الآباء.

**SOUND EFFECTS:** احتكاك التراب بين الأصابع (Foley قريب ومنخفض)، حفيف أوراق الزيتون، طيور الصباح.

**MUSIC:** M1 مستمر — تدخل أول نغمات عود منفردة متباعدة (مقام بياتي على D) عند 00:16.

**TRANSITION TO NEXT SCENE:** Cut ناعم على حركة الصعود: تنتهي الكاميرا في الأغصان المضيئة ← قطع إلى دخان الطابون في ضوء الصباح (Match on light).

**NEGATIVE PROMPT:** NEG-IMAGE + `gloves, dirty nails exaggerated, manicured hands, young hands, sand instead of soil, young sapling, plastic plants`

---

### المشهد 03 — إيقاع الحياة
**الفصل الثاني: فلسطين والحياة قبل التحوّلات الكبرى**

**SCENE NUMBER:** 03

**TIME CODE:** 00:24 – 00:35

**DURATION:** 11 ثانية (3A: 4 ث — 3B: 3.5 ث — 3C: 3.5 ث)

**PURPOSE OF THE SCENE:** إظهار إيقاع الحياة الفلسطينية الريفية كما هو مستمر منذ أجيال (الطابون، الأرض، الأطفال). هذا جسر "خارج الزمن" نحو الأرشيف — **لا يدّعي أنه تصوير من الماضي**؛ الملابس معاصرة/تقليدية حيّة، لا أزياء تاريخية مصطنعة.

**VISUAL DESCRIPTION:** 3A: الجدّة آمنة تُخرج رغيف طابون من الفرن الطيني في فناء حجري. 3B: أحمد يعزق الأرض بين الزيتون على مدرّج. 3C: ثلاثة أطفال يركضون في زقاق حجري منحدر، يتقدمهم يوسف.

**CAMERA ANGLE:** 3A: مستوى العين جالسًا. 3B: مستوى العين، متوسطة-واسعة. 3C: زاوية منخفضة من أسفل الزقاق.

**CAMERA MOVEMENT:** 3A: Handheld خفيف جدًا. 3B: Slow lateral dolly يسارًا. 3C: ثابتة مع تنفّس يدوي، والأطفال يعبرون الكادر.

**LENS:** 3A: 50mm. 3B: 35mm. 3C: 35mm.

**LIGHTING:** صباح مشمس؛ أشعة دافئة منخفضة تخترق الدخان والأزقّة.

**ENVIRONMENT:** L1 — فناء بيت قروي، فرن طابون، مدرّجات، زقاق بدرجات حجرية وعريشة عنب.

**CHARACTER DESCRIPTION:** الحاجّة آمنة (C4)، أحمد (C2)، يوسف (C3) + طفلان آخران بملابس عادية بألوان مكتومة.

**CHARACTER CONSISTENCY NOTES:** التطريز الأحمر العميق على الثوب الأسود لآمنة ثابت. سترة أحمد الزيتية + القميص المربّع الرمادي-الأزرق. يوسف بقميصه الأزرق الفاتح (هنا من دون حقيبة).

**IMAGE GENERATION PROMPT — 03A**
<!-- IMG 03A -->
```text
Cinematic documentary photograph of an 80-year-old Palestinian grandmother baking flatbread in a traditional clay taboun oven in the small stone courtyard of a village house, early morning. She has a round kind face, deep wrinkles and soft brown eyes, a loose white cotton headscarf, and wears a traditional black thobe with deep-red cross-stitch tatreez embroidery on the chest panel, sleeves pushed to the forearms. She lifts a freshly baked, blistered round of taboun bread with her fingertips, focused and calm, with a faint satisfied expression. A low smoke-darkened clay oven at waist level, a wooden board with dough balls dusted with flour, a metal bowl, olive-wood sticks stacked beside her, a limestone wall with a small grapevine. Lighting: low warm sunlight entering from a courtyard opening on the right, soft wisps of smoke catching the light, natural fill bouncing from a whitewashed wall. Medium shot at seated eye level, 50mm prime lens, shallow depth of field, subject on the left third. Natural skin texture, real fabric weave and embroidery detail, restrained warm documentary grade, Kodak Vision3 250D emulation, subtle grain, photorealistic, unposed and authentic, 16:9, no text, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 03A**
<!-- I2V 03A -->
```text
Subtle handheld documentary motion, almost static. The grandmother lifts the bread slowly, turns it over with a natural practiced hand movement and places it on the wooden board; thin smoke rises and curls through the sunbeam; the edge of her headscarf moves slightly; natural blinking and breathing. Hands stay anatomically correct with five fingers, face identity stays stable, the embroidery pattern does not change. 6 seconds, real-time.
```

**IMAGE GENERATION PROMPT — 03B**
<!-- IMG 03B -->
```text
Cinematic documentary photograph of a 46-year-old Palestinian farmer working the soil between olive trees on a stone-walled terrace with a short-handled hoe, mid-morning. Medium-stocky build, sun-tanned skin, short black hair greying at the temples, short dark beard with grey streaks, calm focused expression; faded olive-green work jacket over a blue-grey checkered flannel shirt, worn jeans, dusty brown work boots. Terraced hills dotted with olive and almond trees descend into a valley, scattered limestone houses on the opposite slope. Clear sky with light haze, warm light from a 35-degree sun angle, soft shadows. Medium-wide shot at eye level, 35mm prime lens, the farmer on the right third mid-swing, the terrace wall leading the eye diagonally, moderate depth of field. Restrained documentary grade, muted greens and warm earth tones, Kodak Vision3 250D emulation, subtle grain, natural skin texture, photorealistic, 16:9, no text, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 03B**
<!-- I2V 03B -->
```text
Slow lateral dolly to the left at walking pace. The farmer completes one natural, unhurried hoe stroke into the soil; small clods of earth break apart and a little dust lifts; his jacket fabric moves with his body; olive leaves shimmer in the breeze. Natural human motion with correct weight and timing, no limb distortion, consistent face. 6 seconds.
```

**IMAGE GENERATION PROMPT — 03C**
<!-- IMG 03C -->
```text
Cinematic documentary photograph of three Palestinian village children aged about 8 to 11 running and laughing down a narrow sloping alley of old limestone houses with arched doorways, worn stone steps, potted geraniums and a climbing grapevine overhead, morning. Leading the group is a 10-year-old boy with short dark-brown wavy hair, light olive skin and large dark eyes, wearing a light-blue collared shirt and navy-blue trousers; the other two children wear ordinary modern clothes in muted colors. Shafts of warm sunlight cut across the alley, the rest in soft shade. Shot from a low angle at the bottom of the alley, 35mm prime lens, children mid-stride with slight natural motion blur at the feet, moderate depth of field. Candid, joyful but natural, not staged, realistic child proportions, natural skin texture, restrained documentary grade, Kodak Vision3 250D emulation, subtle grain, photorealistic, 16:9, no text, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 03C**
<!-- I2V 03C -->
```text
Static camera with subtle handheld breathing. The children run down the steps toward and past the camera with a natural gait and realistic foot placement; light shifts across them as they pass through the sunbeams; grapevine leaves sway gently overhead. Correct anatomy, exactly three children, no duplicated children, no merging limbs, no floating. 5 seconds, real-time.
```

**MOTION GRAPHICS:** لا شيء.

**VOICE OVER:** (يبدأ عند 00:25)
> في القرى، يخرجُ الخبزُ من الطابونِ مع أوّلِ الضوء، كما خرجَ منذ أجيال...
> وتجمعُ المواسمُ العائلاتِ حولَ الحقولِ والبيادر.

**SOUND EFFECTS:** طقطقة حطب الزيتون في الطابون، صوت الرغيف على اللوح الخشبي، ضربة معول في التراب، ضحكات أطفال وخطوات على الحجر، ديك ونباح بعيد خافت.

**MUSIC:** Cue M2 «مدن الأمس» يبدأ — العود يطوّر جملته، Pad وتريات ناعم، دفّ (Frame drum) خفيف جدًا.

**TRANSITION TO NEXT SCENE:** **تحوّل لوني إلى الأرشيف:** آخر 12 فريم من 3C تفقد اللون تدريجيًا نحو السيبيا، ثم Cross-dissolve إلى أول صورة أرشيفية مع وميض فيلم خفيف (Light film transition).

**NEGATIVE PROMPT:** NEG-IMAGE + `period costume, Ottoman costume, fez, staged smiles at camera, modern gas oven, metal oven, plastic toys, tourists`

---

### المشهد 04 — صور من زمنٍ مضى (أرشيف)
**الفصل الثاني**

**SCENE NUMBER:** 04

**TIME CODE:** 00:35 – 00:45

**DURATION:** 10 ثوانٍ (4 صور أرشيفية × 2.5 ث)

**PURPOSE OF THE SCENE:** تثبيت الحقيقة التاريخية بصريًا: فلسطين قبل 1948 كانت مدنًا وموانئ وأسواقًا وحياة حضرية وريفية — بصور **حقيقية** فقط.

**VISUAL DESCRIPTION — قائمة لقطات أرشيفية (لا توليد):**
| اللقطة | الموضوع | مصدر مقترح للبحث | كلمات البحث |
|---|---|---|---|
| 4A | تعبئة/تصدير برتقال يافا أو ميناء يافا | Library of Congress — G. Eric and Edith Matson Photograph Collection | `Jaffa oranges`, `Jaffa port`, `Jaffa harbor` |
| 4B | سوق في البلدة القديمة بالقدس | مجموعة ماتسون / المتحف الفلسطيني الرقمي | `Jerusalem market`, `Jerusalem suq` |
| 4C | شارع أو سوق في حيفا أو نابلس أو غزة | مجموعة ماتسون / مؤسسة الدراسات الفلسطينية | `Haifa street`, `Nablus`, `Gaza market` |
| 4D | بيدر/حصاد في قرية | مجموعة ماتسون / أرشيف المتحف الفلسطيني الرقمي | `threshing floor Palestine`, `harvest village` |

**قواعد صارمة للأرشيف:**
- لا تُستخدم صورة إلا إذا كان **سجلّ الفهرسة** يؤكد المكان والتاريخ التقريبي (قبل 1948). انسخ بيانات الكتالوج (رقم السجل، التاريخ، المصوّر) في ملف المصادر.
- لا تلوين، لا Outpainting، لا "تحسين وجوه" بالذكاء الاصطناعي، لا تحريك AI. ترميم الغبار والخدوش فقط، مع الإفصاح.
- راجع حقوق الاستخدام لكل صورة (كثير من مجموعة ماتسون مذكور فيه "No known restrictions" — تحقّق من كل سجل على حدة).

**CAMERA ANGLE:** حسب الصورة الأصلية.

**CAMERA MOVEMENT:** Ken Burns داخل المونتاج فقط: تكبير 3–5% أو Pan أفقي بطيء. اتجاه الحركة يتناوب (يمين/يسار) لخلق إيقاع.

**LENS:** — (أرشيف)

**LIGHTING:** كما في الأصل؛ معالجة Tone خفيفة لتوحيد الكثافة بين الصور.

**ENVIRONMENT:** مدن فلسطين قبل 1948: يافا، القدس، حيفا، نابلس، غزة.

**CHARACTER DESCRIPTION:** أشخاص حقيقيون في صور تاريخية — لا تُنسب إليهم أسماء أو قصص غير موثّقة.

**CHARACTER CONSISTENCY NOTES:** لا ينطبق. تجنّب صورًا يبدو فيها شخص يشبه شخصياتنا التمثيلية لئلا يُفهم أنه هو.

**IMAGE GENERATION PROMPT:** **لا يوجد — أرشيف حقيقي فقط.**
(إذا لم تتوفر صورة أرشيفية مناسبة بحقوق واضحة: احذف اللقطة وأطِل مدة الصور الأخرى؛ لا تولّد بديلًا "تاريخيًا".)

**IMAGE-TO-VIDEO PROMPT:** **لا يوجد.** حركة Ken Burns يدوية في برنامج المونتاج.

**MOTION GRAPHICS:** MG-03 — سطر توثيق صغير أسفل يسار كل صورة (Lower-third أرشيفي): المكان + التاريخ التقريبي + المصدر، مثال القالب: «يافا، نحو 1930 — مكتبة الكونغرس، مجموعة ماتسون» (**املأه من سجل الصورة الفعلي فقط**).

**VOICE OVER:** (يبدأ عند 00:36)
> وفي المدن، كان برتقالُ يافا يعبرُ البحر،
> وكانت القدسُ وحيفا ونابلسُ وغزّةُ عامرةً بالأسواقِ والمدارس.

**SOUND EFFECTS:** طبقة أجواء خافتة جدًا: موج ميناء، حركة سوق بعيدة بالعربية (Levantine Arabic walla) بمعالجة "قديمة" (Low-pass خفيف)، صوت مِرجَح خشبي. خفيفة جدًا كي لا توحي بأنها تسجيل تاريخي.

**MUSIC:** M2 يصل إلى أدفأ نقطة فيه.

**TRANSITION TO NEXT SCENE:** Dissolve من آخر صورة أرشيفية إلى ورق خرائط داكن (Map animation transition).

**NEGATIVE PROMPT:** لا ينطبق (لا توليد). قاعدة بديلة: **ممنوع** أي معالجة AI تولّد تفاصيل غير موجودة في الأصل.

---

### المشهد 05 — الخريطة
**الفصل الثاني**

**SCENE NUMBER:** 05

**TIME CODE:** 00:45 – 00:53

**DURATION:** 8 ثوانٍ

**PURPOSE OF THE SCENE:** تعريف الجمهور العالمي بالجغرافيا: أين تقع فلسطين ومدنها. ثم لحظة التحوّل: ظهور «1948».

**VISUAL DESCRIPTION:** خريطة Motion Graphics بسيطة على خلفية داكنة بملمس ورقي: يُرسم خط الساحل، ثم حدود فلسطين تحت الانتداب البريطاني، ثم تظهر المدن كنقاط مضيئة بأسمائها العربية. تخفت الخريطة ويظهر الرقم «1948».

**CAMERA ANGLE:** Top-down (منظور خريطة).

**CAMERA MOVEMENT:** Push-in افتراضي بطيء (110% ← 115%).

**LENS:** — (Motion Graphics)

**LIGHTING:** خلفية Charcoal مع Vignette ناعم، خطوط Off-White، نقاط المدن Limestone.

**ENVIRONMENT:** فلسطين التاريخية — حدود الانتداب البريطاني (1920–1948).

**CHARACTER DESCRIPTION:** —

**CHARACTER CONSISTENCY NOTES:** —

**IMAGE GENERATION PROMPT:** **لا يُولَّد بالذكاء الاصطناعي.** الخريطة تُبنى يدويًا في After Effects/Illustrator من مصدر موثوق (انظر MG-04 في ملف `05_MOTION_GRAPHICS.md`):
- الساحل والبحر الميت وبحيرة طبريا ونهر الأردن: Natural Earth (بيانات مفتوحة).
- حدود الانتداب: خرائط Survey of Palestine (الأربعينيات)، أو *Atlas of Palestine 1917–1966* لسلمان أبو ستة، أو Palestine Open Maps.
- يمكن توليد **ملمس الخلفية فقط** (ورق داكن) — انظر MG-04 في ملف الموشن.

**IMAGE-TO-VIDEO PROMPT:** لا يوجد (أنيميشن Keyframes).

**MOTION GRAPHICS:** MG-04 — الخريطة:
- 00:45.0 رسم الساحل (Trim path، 1.5 ث).
- 00:46.5 رسم حدود الانتداب (خط 1.5px، 1.5 ث).
- 00:48.0 ظهور المدن تتابعيًا (كل 4 فريمات): القدس، يافا، حيفا، عكا، صفد، الناصرة، نابلس، الخليل، غزة، بئر السبع، اللد، الرملة، بيت لحم.
- 00:50.5 تخفت الخريطة إلى 30%، ويظهر «1948» في المنتصف (Amiri، كبير، Off-White).

**VOICE OVER:** (يبدأ عند 00:46)
> كانت حياةً عاديّة... كحياةِ أيِّ شعبٍ على أرضه.
> حتى عامِ ألفٍ وتسعِمئةٍ وثمانيةٍ وأربعين.

**SOUND EFFECTS:** صوت قلم/حبر خافت جدًا مع رسم الخطوط، "نقرات" ناعمة لظهور المدن، ثم **انسحاب كل الأصوات** مع ظهور «1948».

**MUSIC:** M2 يتوقف فجأة مع ظهور «1948» — يبقى Drone منخفض فقط (Sound drop).

**TRANSITION TO NEXT SCENE:** «1948» يبقى ثانية في الصمت ← Cut إلى أول صورة أرشيفية للنكبة.

**NEGATIVE PROMPT:** لا ينطبق.

---

### المشهد 06 — 1948: النكبة (أرشيف)
**الفصل الثالث: النكبة والتهجير والذاكرة**

**SCENE NUMBER:** 06

**TIME CODE:** 00:53 – 01:09

**DURATION:** 16 ثانية (3–4 صور/مقاطع أرشيفية)

**PURPOSE OF THE SCENE:** شرح موجز ودقيق لما حدث عام 1948 دون مبالغة ودون أرقام غير موثقة. اللحظة الأثقل في الفيلم — تُروى بأكبر قدر من الهدوء.

**VISUAL DESCRIPTION — قائمة لقطات أرشيفية (لا توليد):**
| اللقطة | الموضوع | مصدر مقترح |
|---|---|---|
| 6A | لاجئون فلسطينيون يسيرون على طريق ويحملون أمتعتهم (1948) | UNRWA Photo & Film Archive؛ ICRC Audiovisual Archives؛ المتحف الفلسطيني الرقمي |
| 6B | عائلة لاجئة / أطفال في مخيم خيام مؤقت (1948–1950) | UNRWA Archive؛ UN Photo |
| 6C | (اختياري) مقطع فيلم أرشيفي قصير للنزوح | أرشيفات مرخّصة (British Pathé، Reuters/AP Archive) — بعد التحقق من التاريخ والمكان |
| 6D | (اختياري) خريطة القرى المهجّرة كنقاط | بيانات وليد الخالدي «كي لا ننسى» / Palestine Open Maps — انظر MG-06 |

**قواعد صارمة:** التحقق من أن تاريخ الصورة 1948 (أو 1948–1949) ومكانها فلسطين حسب فهرسة الأرشيف المالك. لا تحريك بالذكاء الاصطناعي لوجوه اللاجئين الحقيقيين. لا تلوين.

**CAMERA ANGLE:** حسب الأصل.

**CAMERA MOVEMENT:** Ken Burns بطيء جدًا (2–3%)؛ قطعات أسرع قليلًا من الفصل السابق (كل 3.5–4 ث).

**LENS:** —

**LIGHTING:** أبيض وأسود كما في الأصل؛ Contrast موحّد؛ Vignette خفيف.

**ENVIRONMENT:** طرق ومخيمات 1948.

**CHARACTER DESCRIPTION:** أشخاص حقيقيون — لا أسماء إلا إن كانت موثقة في سجل الأرشيف.

**CHARACTER CONSISTENCY NOTES:** لا ينطبق.

**IMAGE GENERATION PROMPT:** **لا يوجد — أرشيف حقيقي فقط.**

**IMAGE-TO-VIDEO PROMPT:** **لا يوجد.**

**MOTION GRAPHICS:**
- MG-02: عنوان «النكبة» في منتصف الشاشة على أول صورة (00:54–00:57)، صغير وهادئ.
- MG-05: بطاقة رقم موثّق (01:01–01:06) أسفل الكادر: «أكثر من 700,000 فلسطيني هُجِّروا من مدنهم وقراهم» وتحتها سطر المصدر: «المصادر: الأونروا؛ لجنة التوفيق الدولية التابعة للأمم المتحدة».
- MG-03: سطر توثيق لكل صورة أرشيفية.

**VOICE OVER:** (يبدأ عند 00:55)
> في خضمِّ حربِ ذلك العام، ومع نهايةِ الانتدابِ البريطانيّ وقيامِ دولةِ إسرائيل،
> هُجِّرَ أكثرُ من سبعمئةِ ألفِ فلسطينيٍّ من مدنِهم وقراهم،
> وأُفرِغَت مئاتُ القرى من أهلِها.
> سمّى الفلسطينيون ما حدث: النكبة.

> **التحقق:** «أكثر من 700 ألف» يتّسق مع تقدير الأونروا (نحو 750 ألفًا) ولجنة التوفيق الدولية (نحو 711 ألفًا). «مئات القرى» يتّسق مع توثيق وليد الخالدي (418 قرية). انظر `08_SOURCES.md`.

**SOUND EFFECTS:** شبه صمت. ريح باردة خافتة جدًا، خطوات بعيدة على الحصى (منخفضة جدًا). **لا** أصوات انفجارات أو رصاص.

**MUSIC:** Cue M3 «النكبة» — Cello منفرد طويل النفَس بلون مقام الحجاز على D، فوق Drone. بلا إيقاع.

**TRANSITION TO NEXT SCENE:** Slow fade إلى لون مُطفأ: من آخر صورة أرشيفية بالأبيض والأسود إلى أقدام العائلة في 7A (ألوان شبه منطفئة) — يربط الماضي بالمشهد التمثيلي دون إيهام بأنه أرشيف.

**NEGATIVE PROMPT:** لا ينطبق. ممنوع: أي صور عنف دموي، جثث، أو صور غير موثقة التاريخ.

---

### المشهد 07 — الطريق (مشهد تمثيلي)
**الفصل الثالث**

**SCENE NUMBER:** 07

**TIME CODE:** 01:09 – 01:18

**DURATION:** 9 ثوانٍ (7A: 4.5 ث — 7B: 4.5 ث)

**PURPOSE OF THE SCENE:** نقل التجربة الإنسانية للنزوح دون عنف ودون تزييف تاريخ: **مشهد رمزي** بلا وجوه، مُعلَن أنه تمثيلي. الطفل الصغير الممسك بيد أمّه هو — رمزيًا — أبو خليل في الثامنة من عمره.

**VISUAL DESCRIPTION:** 7A: لقطة منخفضة على مستوى الأرض لأقدام عائلة تمشي على طريق ترابي: صندل امرأة تحت طرف ثوب مطرّز داكن، حذاء رجل قديم، قدما طفل صغير؛ يد الطفل تمسك يد الأم أعلى الكادر؛ صرّة قماش معلّقة. 7B: لقطة واسعة جدًا من الخلف لعائلة من خمسة أشخاص صغار في الكادر يسيرون على طريق متعرّج بين تلال جرداء عند الغسق.

**CAMERA ANGLE:** 7A: مستوى الأرض. 7B: أعلى قليلًا من مستوى العين، بعيد.

**CAMERA MOVEMENT:** 7A: Follow بطيء خلف الأقدام. 7B: Locked-off مع Push-in بالغ البطء.

**LENS:** 7A: 35mm. 7B: 50mm.

**LIGHTING:** سماء خريفية ملبّدة، ضوء منتشر بارد، تباين منخفض.

**ENVIRONMENT:** طريق ريفي ترابي، تلال جرداء، زيتونة وحيدة.

**CHARACTER DESCRIPTION:** عائلة ريفية بلا وجوه ظاهرة؛ ملابس بسيطة داكنة بلا تفاصيل "تاريخية" مبالغ فيها.

**CHARACTER CONSISTENCY NOTES:** لا وجوه. الطفل الصغير بصندل — يُستحضر لاحقًا في م17 حين يسلّم الجدّ المفتاح لحفيده (دائرة مكتملة).

**IMAGE GENERATION PROMPT — 07A**
<!-- IMG 07A -->
```text
Cinematic documentary reconstruction photograph, close low-angle shot at ground level of the feet of a rural family walking away along a dusty unpaved country road: an adult woman's feet in worn leather sandals beneath the dark hem of a long embroidered dress, an adult man's feet in old scuffed leather shoes, and a small boy's feet in simple sandals, all walking away from the camera. At the top edge of the frame, the boy's small hand holds the woman's hand. A cloth bundle tied with rope hangs from the man's hand. No faces visible. Late afternoon, overcast autumn sky, diffused cool light, soft dust lifting from the road. 35mm prime lens at road level, shallow depth of field, feet sharp, the road and dry hills receding into soft focus. Muted, heavily desaturated color grade with cool shadows, almost colorless but not black and white, Kodak Vision3 film emulation, visible fine film grain, photorealistic, quiet and dignified, no violence, 16:9, no text, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 07A**
<!-- I2V 07A -->
```text
The camera follows slowly from behind at ground level as the feet walk away along the dusty road with natural, tired, unhurried steps; fine dust rises and drifts; the cloth bundle sways with each step; the child's steps are shorter and quicker than the adults'. Natural gait, correct number of feet and legs, feet grounded, no sliding or floating. 6 seconds.
```

**IMAGE GENERATION PROMPT — 07B**
<!-- IMG 07B -->
```text
Cinematic documentary reconstruction photograph, extreme wide shot of a small rural family seen from behind, walking away along a winding dirt road that crosses bare rolling hills at dusk under a heavy overcast sky. Five small figures: a man carrying a cloth bundle on his shoulder, a woman balancing a bundle on her head, an elderly woman, and two children, the smaller boy holding the woman's hand. The figures are small in the lower third of the frame, faces not visible, simple dark rural clothing in muted tones. A lone olive tree on the left, distant hills fading into haze. Cold, diffused, low-contrast light, a muted desaturated palette leaning toward grey-green and dust, 50mm lens from a slightly elevated position, deep focus. Fine film grain, photorealistic, restrained and humane, no violence, no soldiers, no vehicles, 16:9, no text, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 07B**
<!-- I2V 07B -->
```text
Locked-off wide shot with an extremely slow push-in. The small figures walk slowly away along the road at a natural, consistent pace; low clouds drift slowly; dry grass moves in a cold wind; the light dims very slightly. The figure count stays exactly five, no merging, no duplication, no sliding. 6 seconds.
```

**MOTION GRAPHICS:** MG-07 — وسم صغير أعلى يمين الكادر بشفافية 60%: «مشهد تمثيلي» (Reconstruction).

**VOICE OVER:** (يبدأ عند 01:10)
> حملوا ما استطاعوا حملَه...
> وظنَّ كثيرون أنّ الغيابَ لن يطولَ أكثرَ من أيام.

**SOUND EFFECTS:** خطوات على طريق ترابي وحصى، حفيف قماش الصرّة، ريح خريفية باردة، غراب بعيد واحد.

**MUSIC:** M3 مستمر — تدخل Strings منخفضة جدًا تحت الـ Cello.

**TRANSITION TO NEXT SCENE:** Slow fade إلى أسود لمدة 6 فريمات ← Fade-in على المفتاح في ضوء النافذة الدافئ (انتقال من البرودة إلى الدفء = من الحدث إلى الذاكرة).

**NEGATIVE PROMPT:** NEG-IMAGE + `visible faces, crying faces, soldiers, weapons, trucks, tanks, explosions, smoke, burning houses, modern clothing, sneakers, plastic bags, black-and-white archival imitation, sepia fake photo`

---

### المشهد 08 — المفتاح
**الفصل الثالث**

**SCENE NUMBER:** 08

**TIME CODE:** 01:18 – 01:30

**DURATION:** 12 ثانية (8A: 7 ث — 8B: 5 ث)

**PURPOSE OF THE SCENE:** قلب الفيلم الرمزي. المفتاح كجسر بين البيت المفقود والذاكرة الحيّة. أول ظهور لوجه أبو خليل.

**VISUAL DESCRIPTION:** 8A: Macro لمفتاح حديدي يدوي الصنع (~15 سم) بعروة بيضاوية كبيرة وصدأ خفيف، في كفّ أبو خليل المفتوحة، غبار يسبح في شعاع النافذة. 8B: بورتريه لأبو خليل جالسًا قرب النافذة يمسك المفتاح عند صدره وينظر خارجًا — تعبير هادئ متماسك، لا دموع.

**CAMERA ANGLE:** 8A: من أعلى الكف قليلًا. 8B: Medium close-up بمستوى العين.

**CAMERA MOVEMENT:** 8A: Slow orbit (~15°) حول المفتاح مع Focus pull. 8B: Push-in بالغ البطء.

**LENS:** 8A: 100mm macro. 8B: 85mm.

**LIGHTING:** ضوء نافذة جانبي من اليسار وقت العصر، Rembrandt light ناعم على الوجه، ظلال دافئة عميقة.

**ENVIRONMENT:** L2 — بيت أبو خليل: جدار أبيض، خزانة خشبية، صورة قديمة مؤطرة غير مقروءة.

**CHARACTER DESCRIPTION:** أبو خليل (C1).

**CHARACTER CONSISTENCY NOTES:** **ثبّت المفتاح:** نفس الشكل في 8A و8B و17A (عروة بيضاوية، ساق طويلة، لسان مستطيل بسيط). ولّد المفتاح أولًا كـ Object reference. الخاتم الفضي، الكوفية على الكتفين لا على الرأس.

**IMAGE GENERATION PROMPT — 08A**
<!-- IMG 08A -->
```text
Cinematic documentary macro photograph of an old hand-forged iron house key, about 15 centimeters long, with a large oval bow, a long shaft and a simple rectangular bit, dark patina with traces of rust, worn smooth where generations of fingers held it, resting diagonally across the open palm of an 86-year-old Palestinian man. His palm is deeply lined, with a plain thin silver ring on the right ring finger and the cuff of a charcoal-grey wool jacket at the frame edge. Interior of a modest village home, soft late-afternoon window light from the left, warm dust particles floating in the beam, dark warm background falling into shadow. 100mm macro lens, camera slightly above the palm, key positioned diagonally from lower left to upper right, extremely shallow depth of field with the key's bit in razor-sharp focus. Rich tactile textures of iron and skin, restrained warm grade with deep but clean shadows, Kodak Vision3 500T emulation, subtle grain, photorealistic, intimate and reverent, 16:9, no text, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 08A**
<!-- I2V 08A -->
```text
Very slow orbital arc of about 15 degrees around the key from left to right, with a gentle focus pull traveling from the key's bit to its oval bow. The old man's fingers close slightly around the key with a tiny natural tremor of age; dust particles drift through the window beam. The key's shape stays absolutely rigid and consistent, hand anatomy stable, the ring stays on the same finger, no morphing. 7 seconds.
```

**IMAGE GENERATION PROMPT — 08B**
<!-- IMG 08B -->
```text
Cinematic documentary portrait of an 86-year-old Palestinian man sitting by a window inside his modest stone home, holding an old hand-forged iron key with a large oval bow loosely against his chest. Lean build, deeply lined sun-weathered olive-brown skin, short neatly trimmed white beard, thin white hair, warm dark-brown eyes with slight age clouding looking off-camera toward the window, a quiet, composed expression of memory, no tears. A white-and-black checkered keffiyeh draped loosely over his shoulders, charcoal-grey wool jacket over a faded beige collarless shirt, a plain thin silver ring on his right ring finger. Background: a whitewashed wall softly out of focus with a small framed faded photograph and an old wooden cabinet. Lighting: soft late-afternoon window light from camera left, gentle Rembrandt light on the face, deep warm falloff. Medium close-up at eye level, 85mm prime lens, shallow depth of field, eyes in critical focus, subject on the right third looking into the frame. Natural skin texture with pores, wrinkles and slight imperfections, restrained warm grade, Kodak Vision3 500T emulation, subtle grain, photorealistic, dignified, 16:9, no text, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 08B**
<!-- I2V 08B -->
```text
Extremely slow push-in on the face. The old man breathes slowly; his eyes blink naturally once and then shift subtly from the window down toward the key in his hands; a very slight movement of the lips as if about to speak, but he stays silent. Dust floats in the window light. Face identity, beard shape and wrinkles remain consistent, no facial morphing, no exaggerated emotion. 7 seconds.
```

**MOTION GRAPHICS:** لا شيء (اترك المفتاح يتكلم).

**VOICE OVER:** (يبدأ عند 01:19)
> ولذلك، احتفظَ كثيرون منهم بمفاتيحِ بيوتِهم.
> مفتاحٌ حديديٌّ قديم... لم يعُد يفتحُ بابًا،
> لكنّه ما زال يفتحُ الذاكرة.

**SOUND EFFECTS:** رنين معدني خفيف للمفتاح حين تنغلق عليه الأصابع (Foley قريب)، دقّات ساعة حائط بعيدة، أجواء غرفة هادئة، طائر خارج النافذة.

**MUSIC:** Cue M3b — **عود منفرد** يعزف الجملة الرئيسية للفيلم لأول مرة كاملة، ببطء (مقام بياتي).

**TRANSITION TO NEXT SCENE:** Cut على حركة اليد: من أصابع تنغلق على المفتاح (8A/8B) إلى أصابع تقلب صفحة الألبوم (9A) — Match cut على اليد.

**NEGATIVE PROMPT:** NEG-IMAGE + `tears, crying, theatrical sadness, modern key, Yale key, keyring, key changing shape, keffiyeh on head, young man, clean smooth skin`

---

### المشهد 09 — الذاكرة
**الفصل الثالث**

**SCENE NUMBER:** 09

**TIME CODE:** 01:30 – 01:39

**DURATION:** 9 ثوانٍ (9A: 5 ث — 9B: 4 ث)

**PURPOSE OF THE SCENE:** الذاكرة كفعل مستمر: صور قديمة، أسماء قرى تُحكى، وأطلال بيت حجري يحرسها الصبّار — رمز القرى المهجّرة.

**VISUAL DESCRIPTION:** 9A: يدا أبو خليل تقلبان صفحات ألبوم صور قديم بصفحات كرتون أسود، صور صغيرة بالأبيض والأسود **ضبابية بلا وجوه مقروءة**، كوب شاي بجانبه. 9B: أطلال بيت حجري بلا سقف، قوس باب ما زال قائمًا، الصبّار في المقدّمة، زيتون ولوز بري حوله.

**CAMERA ANGLE:** 9A: من أعلى بزاوية 45°. 9B: مستوى العين عبر ألواح الصبار.

**CAMERA MOVEMENT:** 9A: ثابتة مع انجراف يدوي طفيف. 9B: Slow dolly forward عبر الصبار نحو القوس.

**LENS:** 9A: 50mm. 9B: 35mm.

**LIGHTING:** 9A: ضوء نافذة عصر دافئ (استمرار م8). 9B: غيوم ناعمة آخر النهار، ضوء بارد هادئ.

**ENVIRONMENT:** L2 (داخلي) ← تلّة بأطلال بيت قروي.

**CHARACTER DESCRIPTION:** أبو خليل (C1) — يداه فقط.

**CHARACTER CONSISTENCY NOTES:** الخاتم + الكمّ الرمادي. **الصور داخل الألبوم:** يجب أن تبقى ضبابية في التوليد؛ في المونتاج يمكن تركيب صور عائلية حقيقية (أرشيف العائلة المنتجة أو صور مرخّصة من المتحف الفلسطيني الرقمي) فوق الصفحات عبر Tracking — بإذن أصحابها.

**IMAGE GENERATION PROMPT — 09A**
<!-- IMG 09A -->
```text
Cinematic documentary close-up of elderly hands slowly turning the thick black cardboard pages of an old family photo album resting on a worn wooden table, beside a small glass of tea. The album holds small vintage black-and-white and sepia photographs with deckled white borders held by paper photo corners; the photographs are softly out of focus so that no faces can be read. The hands belong to an 86-year-old man, with a plain thin silver ring on the right ring finger and a charcoal-grey wool jacket cuff. Soft late-afternoon window light from the left, warm and gentle, dust in the air. Camera at a 45-degree high angle, 50mm prime lens, shallow depth of field with focus on the fingertips and the page edge. Worn paper textures, restrained warm grade, Kodak Vision3 500T emulation, subtle grain, photorealistic, quiet and intimate, 16:9, no text, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 09A**
<!-- I2V 09A -->
```text
Static camera with a very subtle handheld drift. The hand turns one album page slowly and naturally; the page bends with realistic paper physics and settles flat; a faint shadow passes across the photographs; the tea surface trembles slightly. Five fingers, stable anatomy, the photographs stay blurred and never morph into faces. 5 seconds.
```

**IMAGE GENERATION PROMPT — 09B**
<!-- IMG 09B -->
```text
Cinematic documentary photograph of the roofless ruins of an old limestone village house on a hillside, its arched doorway still standing, overgrown with wild grass and fig shoots, with a large clump of prickly pear cactus in the soft foreground; scattered dressed stones on the ground; olive and almond trees growing wild around it; distant hills under a soft overcast late-afternoon sky. Medium-wide shot at eye level through the out-of-focus cactus pads, 35mm prime lens, the arched doorway on the right third, moderate depth of field. Cool, quiet, slightly desaturated grade, muted greens and pale stone, Kodak Vision3 250D emulation, fine film grain, photorealistic, contemplative, no people, no graffiti, no flags, 16:9, no text, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 09B**
<!-- I2V 09B -->
```text
Slow dolly forward past the out-of-focus cactus pads toward the standing arch, revealing it gradually; wild grass moves in a light wind; clouds drift slowly overhead. The stones and the arch remain rigid and stable, no warping. 5 seconds.
```

**MOTION GRAPHICS:** MG-02 (اختياري) — «الذاكرة» صغيرة أسفل يمين الكادر على 9B.

**VOICE OVER:** (يبدأ عند 01:31)
> صورٌ قديمة، وأسماءُ قرى تُروى للأحفاد...
> فالذاكرةُ هنا ليست حنينًا فحسب... بل وصيّة.

**SOUND EFFECTS:** تقليب صفحة كرتون، رنّة خفيفة لملعقة في كوب الشاي، ثم في 9B: ريح في العشب، حشرات مسائية خافتة. **في آخر ثانية:** يبدأ صوت جرس مدرسة وأطفال بعيدين (Sound bridge / J-cut).

**MUSIC:** M3 يتلاشى ببطء؛ العود يبقى ونغمة معلّقة.

**TRANSITION TO NEXT SCENE:** **J-cut صوتي:** أصوات المدرسة تسبق الصورة بثانية، ثم Cut إلى يوسف يمشي في ضوء الصباح (انتقال من البرودة إلى ضوء جديد = جيل جديد).

**NEGATIVE PROMPT:** NEG-IMAGE + `readable faces in photos, sharp faces in photos, modern color photos, smartphone, graffiti, flags, people in ruins, horror atmosphere, dramatic storm`

---

### المشهد 10 — الأجيال الجديدة
**الفصل الرابع: الحياة الفلسطينية المعاصرة**

**SCENE NUMBER:** 10

**TIME CODE:** 01:39 – 01:48

**DURATION:** 9 ثوانٍ (10A: 5 ث — 10B: 4 ث)

**PURPOSE OF THE SCENE:** نقلة نحو الحاضر والحياة: يوسف حفيد أبو خليل في طريقه إلى المدرسة، ثم الصف — طاقة، فضول، طفولة طبيعية.

**VISUAL DESCRIPTION:** 10A: يوسف يمشي على طريق قروي صباحًا بحقيبته، جدار سنسلة وزيتون، بيوت بخزانات سوداء، طفلان آخران بعيدًا. 10B: صف مدرسي بسيط لأولاد (9–11 عامًا) على مقاعد خشبية، أيدٍ مرفوعة، سبورة خضراء بعلامات غير مقروءة، يوسف في الصف الثاني يبتسم لزميله.

**CAMERA ANGLE:** 10A: مستوى عين الطفل، ¾ أمامي. 10B: من جانب الصف بمستوى العين.

**CAMERA MOVEMENT:** 10A: Tracking للخلف بسرعة مشي الطفل. 10B: Handheld خفيف مع انجراف يمينًا.

**LENS:** 35mm للّقطتين.

**LIGHTING:** 10A: شمس صباح منخفضة خلف الطفل (Backlight على الشعر). 10B: ضوء نهار ناعم من نوافذ يسار الصف.

**ENVIRONMENT:** L1 + مدرسة حكومية بسيطة: جدران خضراء فاتحة، رسومات أطفال، نوافذ بإطارات معدنية.

**CHARACTER DESCRIPTION:** يوسف (C3) + زملاء من الأولاد بملامح متنوعة وملابس مدرسية عادية.

**CHARACTER CONSISTENCY NOTES:** القميص الأزرق الفاتح، البنطال الكحلي، الحقيبة الزرقاء الداكنة بحزام مهترئ. ملاحظة دقة: كثير من المدارس الفلسطينية في هذه المرحلة مفصولة حسب الجنس، لذلك الصف هنا للأولاد.

**IMAGE GENERATION PROMPT — 10A**
<!-- IMG 10A -->
```text
Cinematic documentary photograph of a 10-year-old Palestinian boy walking to school along a quiet village road in the early morning, seen in a three-quarter front view. Slim, light olive skin, short dark-brown wavy hair, large dark eyes, a curious, alert, slightly sleepy expression; light-blue collared shirt, navy-blue trousers, scuffed white sneakers, a worn dark-blue backpack with one frayed strap. The road is lined with a low dry-stone wall, olive trees and a few limestone houses with black water tanks on their roofs; two other schoolchildren walk in the distance. Clear weather, low warm morning sun backlighting his hair, soft natural fill. Medium-wide shot at the child's eye level, 35mm prime lens, the boy on the left third walking into the frame, shallow-to-moderate depth of field. Natural skin texture, realistic child proportions, restrained documentary grade, Kodak Vision3 250D emulation, subtle grain, photorealistic, hopeful and ordinary, 16:9, no text, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 10A**
<!-- I2V 10A -->
```text
Smooth, slow tracking shot moving backward at the boy's walking pace with slight natural handheld sway. He walks with a relaxed natural gait, adjusts his backpack strap once, and glances briefly toward the sun; his hair and shirt move lightly; olive leaves sway at the roadside. Realistic walking cycle, feet grounded, no sliding, consistent face. 6 seconds.
```

**IMAGE GENERATION PROMPT — 10B**
<!-- IMG 10B -->
```text
Cinematic documentary photograph inside a simple Palestinian public school classroom for boys: about twenty boys aged 9 to 11 sitting at worn wooden two-seat desks, a few raising their hands, one reading aloud from a textbook; in the second row a 10-year-old boy with short dark-brown wavy hair, light olive skin and a light-blue collared shirt smiles at the classmate beside him. Pale-green painted walls, a large green chalkboard with chalk marks blurred and unreadable, metal-framed windows letting in bright soft daylight from the left, children's drawings pinned on the wall slightly out of focus. Eye-level medium-wide shot from the side of the room, 35mm prime lens, moderate depth of field, the boy in sharp focus. Lively and natural, realistic faces with diverse features, natural skin texture, restrained documentary grade, subtle grain, photorealistic, 16:9, no readable text, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 10B**
<!-- I2V 10B -->
```text
Subtle handheld documentary motion with a slow drift to the right. The students move naturally: a few hands go up, one boy turns his head to whisper and smile, pages turn, light dust floats in the window light. No warping faces, no duplicated children, consistent desk geometry. 5 seconds.
```

**MOTION GRAPHICS:** لا شيء.

**VOICE OVER:** (يبدأ عند 01:40)
> واليوم، يحملُ جيلٌ جديدٌ هذه الوصيّةَ في حقائبِ المدرسة...
> إلى جانبِ الكتبِ والأحلام.

**SOUND EFFECTS:** جرس مدرسة، خطوات على طريق، أطفال يتنادون بالعربية من بعيد، ثم داخل الصف: همهمة تلاميذ، حكّ طباشير، تقليب صفحات.

**MUSIC:** Cue M4 «الحياة» — نبض يعود: إيقاع يدوي ناعم (~72 BPM)، عود + Pizzicato وتريات، لون أخفّ.

**TRANSITION TO NEXT SCENE:** Cross-dissolve قصير (12 فريم) من الصف إلى أغصان الزيتون المضاءة.

**NEGATIVE PROMPT:** NEG-IMAGE + `school uniform logos, readable writing on board, girls in boys classroom inconsistently, modern luxury school, computers everywhere, posed group photo, children looking at camera`

---

### المشهد 11 — الزيتون
**الفصل الرابع**

**SCENE NUMBER:** 11

**TIME CODE:** 01:48 – 01:57

**DURATION:** 9 ثوانٍ (11A: 5 ث — 11B: 4 ث)

**PURPOSE OF THE SCENE:** موسم قطاف الزيتون كطقس عائلي سنوي وعهد مع الأرض. ثلاثة أجيال في المشهد نفسه دلاليًا (أحمد ويوسف، وأشجار عمرها قرون).

**VISUAL DESCRIPTION:** 11A: أحمد على سلّم خشبي قصير يمشّط الزيتون بيديه، وتحته على شوادر بلاستيكية فوق التربة الحمراء امرأتان ويوسف يجمعون الحبّات في دلاء وأكياس. 11B: Macro ليدي أحمد تحتضنان حفنة زيتون أخضر وأسود مع أوراق فضية.

**CAMERA ANGLE:** 11A: مستوى العين، متوسطة-واسعة. 11B: Macro من الجانب.

**CAMERA MOVEMENT:** 11A: Pedestal/crane down بطيء من الأغصان إلى العائلة. 11B: Locked-off مع Push-in بطيء.

**LENS:** 11A: 35mm. 11B: 100mm macro.

**LIGHTING:** ضحى خريفي صافٍ، ضوء متسلل عبر الأوراق (Dappled light)، أوراق مضاءة من الخلف.

**ENVIRONMENT:** L1 — كرم زيتون مدرّج في الخريف (موسم القطاف: أكتوبر–نوفمبر).

**CHARACTER DESCRIPTION:** أحمد (C2)، يوسف (C3)، امرأتان من العائلة (منديل رأس وملابس عمل عادية).

**CHARACTER CONSISTENCY NOTES:** نفس سترة أحمد الزيتية. يوسف بنفس القميص الأزرق (بلا حقيبة). نفس لون التربة الحمراء كما في م2.

**IMAGE GENERATION PROMPT — 11A**
<!-- IMG 11A -->
```text
Cinematic documentary photograph of a Palestinian family olive harvest in an autumn grove on terraced hills: a 46-year-old farmer with short black hair greying at the temples and a short dark beard with grey streaks, wearing a faded olive-green work jacket over a blue-grey checkered flannel shirt, stands on a short wooden ladder combing olives from the branches with his hands; below him, on large tarps spread over the red soil, two women in headscarves and simple work clothes and a 10-year-old boy in a light-blue collared shirt gather fallen olives into buckets and woven sacks. Mid-morning, clear autumn sky, warm low sun filtering through the silver-green leaves, dappled light on the tarps. Medium-wide shot at eye level, 35mm prime lens, the farmer on the upper right third, the family in the lower-left foreground, moderate depth of field. Green and black olives clearly visible, realistic tools, natural candid poses, natural skin texture, restrained warm documentary grade, Kodak Vision3 250D emulation, subtle grain, photorealistic, 16:9, no text, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 11A**
<!-- I2V 11A -->
```text
Slow gentle pedestal-down from canopy level to the family on the ground with a slight forward drift. The farmer's hands strip olives from a branch, the olives fall naturally and bounce on the tarp; the women and the boy gather olives with natural movements; leaves flutter in the breeze. Correct anatomy, consistent faces, no floating olives. 7 seconds.
```

**IMAGE GENERATION PROMPT — 11B**
<!-- IMG 11B -->
```text
Cinematic documentary macro photograph of a farmer's strong, sun-tanned, work-worn hands holding a cupped handful of freshly picked green and purple-black olives with a few silver-green leaves, above a tarp covered with olives. The cuff of a faded olive-green jacket and a blue-grey checkered shirt cuff are visible. Autumn morning light from behind and the side, backlit leaves glowing, warm highlights on the glossy olive skins. 100mm macro lens, shallow depth of field, hands centered, a background of olive branches in soft bokeh. Natural skin texture with small cuts and calluses, restrained warm grade, subtle grain, photorealistic, 16:9, no text, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 11B**
<!-- I2V 11B -->
```text
Locked-off shot with a very slow push-in. A few olives roll naturally within the cupped hands and one drops to the tarp below; backlit leaves tremble in the breeze. Five fingers on each hand, olives keep their shape, no morphing. 5 seconds.
```

**MOTION GRAPHICS:** لا شيء.

**VOICE OVER:** (يبدأ عند 01:49)
> وفي كلِّ خريف، تعودُ العائلاتُ إلى حقولِ الزيتون...
> كأنّها تُجدِّدُ عهدًا قديمًا مع الأرض.

**SOUND EFFECTS:** حبّات زيتون تتساقط على الشادر (صوت مميّز ومهم)، حفيف أغصان، أحاديث عائلية خافتة بالعربية، صرير سلّم خشبي.

**MUSIC:** M4 يتصاعد قليلًا — العود يتبادل الجملة مع الوتريات.

**TRANSITION TO NEXT SCENE:** Cut على الإيقاع (Beat cut) إلى حركة السوق.

**NEGATIVE PROMPT:** NEG-IMAGE + `machinery, tractors, olive shaking machine, perfect identical olives, plastic fruit, spring blossoms, green summer grass`

---

### المشهد 12 — المدينة
**الفصل الرابع**

**SCENE NUMBER:** 12

**TIME CODE:** 01:57 – 02:07

**DURATION:** 10 ثوانٍ (12A: 3.5 ث — 12B: 3 ث — 12C: 3.5 ث)

**PURPOSE OF THE SCENE:** الحياة الحضرية الفلسطينية المعاصرة كما هي: أسواق، مقاهٍ، شباب، عمل — مع إشارة هادئة إلى الحواجز والقيود دون عرض صادم.

**VISUAL DESCRIPTION:** 12A: سوق حجري مقبّب في مدينة كنابلس ينفتح على شارع مشمس: بهارات، صواني كنافة، عربة، متسوّقون. 12B: شباب وشابات في مقهى رصيف في رام الله عند المساء. 12C: أسطح مدينة على تلال عند الساعة الذهبية — خزانات سوداء، سخانات شمسية، مآذن وبرج كنيسة، حمام يطير.

**CAMERA ANGLE:** 12A: مستوى العين. 12B: مستوى العين جالسًا. 12C: منظر مرتفع.

**CAMERA MOVEMENT:** 12A: Handheld مع Push forward. 12B: Lateral slide بطيء. 12C: Pan بطيء يسار ← يمين.

**LENS:** 12A: 35mm. 12B: 50mm. 12C: 50mm (ضغط الطبقات).

**LIGHTING:** ضحى مضبّب داخل السوق ← غسق دافئ ← ساعة ذهبية.

**ENVIRONMENT:** L3.

**CHARACTER DESCRIPTION:** شخصيات ثانوية متنوعة: نساء بحجاب وبدونه، شباب بحقائب، باعة.

**CHARACTER CONSISTENCY NOTES:** لا شخصيات رئيسية. تجنّب أي لافتات مقروءة (التوليد يكتب عربية خاطئة).

> **توصية إنتاجية قوية:** هذا المشهد يكسب كثيرًا من **لقطات حقيقية** مرخّصة أو مصوّرة من مصوّرين فلسطينيين محليين؛ المدن الحقيقية أغنى وأدقّ من أي توليد. استخدم الـ Prompts كخطة بديلة.

**IMAGE GENERATION PROMPT — 12A**
<!-- IMG 12A -->
```text
Cinematic documentary photograph of a busy street in the old commercial center of a Palestinian West Bank city such as Nablus, late morning: a covered stone market passage with high vaulted arches opening onto a sunlit street, shopfronts with sacks of spices, trays of knafeh, hanging clothes, a man pushing a hand cart, shoppers of all ages in modern everyday clothes, some women in headscarves and some without, a few young men with backpacks. Shop signs present but blurred and unreadable. Hazy sunlight spilling through the arch opening, warm stone tones, mixed shade. Eye-level medium-wide shot, 35mm lens, layered composition with foreground figures slightly out of focus, natural motion blur on a passer-by. Authentic, lively, everyday, not exoticized, natural skin textures, restrained documentary grade, subtle grain, photorealistic, 16:9, no readable text, no logos, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 12A**
<!-- I2V 12A -->
```text
Subtle handheld documentary motion with a slow push forward through the crowd. People walk naturally in different directions at believable speeds, the cart rolls forward, a shopkeeper hands a bag to a customer; sunlit dust is visible under the arch. No sliding feet, no merging people, stable faces, the arches remain rigid. 5 seconds.
```

**IMAGE GENERATION PROMPT — 12B**
<!-- IMG 12B -->
```text
Cinematic documentary photograph of young Palestinians in their twenties at a small sidewalk café in Ramallah in the early evening: two young women and two young men around a small table with cups of coffee and tea, one laughing, one looking at a phone, one gesturing in conversation; casual modern clothing, one of the women wears a headscarf and the other does not. Behind them a sloping street with parked cars, limestone-clad buildings, warm shop lights turning on and a soft dusk sky. Medium shot from across the table at seated eye level, 50mm prime lens, shallow depth of field, a natural candid moment. Natural skin textures, realistic faces, restrained warm grade, Kodak Vision3 500T emulation, subtle grain, photorealistic, 16:9, no readable text, no logos, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 12B**
<!-- I2V 12B -->
```text
Gentle slow lateral slide. Natural conversation: one young man laughs, a woman sips her coffee and puts the cup down, another turns to listen; a car passes softly out of focus in the background. Natural lip and eye movement, no facial distortion, cups keep their shape. 5 seconds.
```

**IMAGE GENERATION PROMPT — 12C**
<!-- IMG 12C -->
```text
Cinematic documentary photograph, wide view over the rooftops of a Palestinian hill city such as Bethlehem at golden hour: dense limestone buildings of different ages climbing the slopes, rooftops crowded with black water tanks, solar water heaters and satellite dishes, a few minarets and a church bell tower on the skyline, laundry on a line, pigeons in flight, surrounding hills with olive groves fading into warm haze. Elevated viewpoint, 50mm lens compressing the layers, deep focus. Warm low sun from the right, long soft shadows. Restrained warm, natural grade, Kodak Vision3 250D emulation, subtle grain, photorealistic, 16:9, no text, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 12C**
<!-- I2V 12C -->
```text
Very slow pan from left to right across the rooftops; pigeons circle naturally; laundry moves in the breeze; the sunlight warms subtly. Buildings remain completely rigid, no warping. 6 seconds.
```

**MOTION GRAPHICS:** لا شيء.

**VOICE OVER:** (يبدأ عند 01:58)
> وفي المدن، تمضي الحياةُ بإيقاعِها اليوميّ:
> أسواقٌ ومقاهٍ، طلّابٌ وعمّال...
> حياةٌ تستمرّ، رغمَ الحواجزِ والقيود.

**SOUND EFFECTS:** سوق بالعربية الشامية (نداءات باعة، أكياس، عربة)، فناجين على صحون، ضحكات، سيارات بعيدة، أذان بعيد خافت جدًا أو أجراس كنيسة (أحدهما فقط)، رفرفة حمام.

**MUSIC:** M4 يكمل ثم يهدأ تدريجيًا في آخر 3 ثوانٍ.

**TRANSITION TO NEXT SCENE:** **Match on light:** شمس الأسطح الذهبية (12C) ← Cross-dissolve (36 فريم) إلى شمس غروب فوق بحر غزة (13A).

**NEGATIVE PROMPT:** NEG-IMAGE + `readable Arabic signs, misspelled signage, brand logos, Gulf malls, skyscrapers, palm-lined boulevards, exoticized bazaar, belly dancers, hookah cliché focus`

---

### المشهد 13 — غزة والبحر
**الفصل الخامس: غزة والإنسان الفلسطيني**

**SCENE NUMBER:** 13

**TIME CODE:** 02:07 – 02:19

**DURATION:** 12 ثانية (13A: 6 ث — 13B: 6 ث)

**PURPOSE OF THE SCENE:** تقديم غزة عبر البحر والرزق والإنسان — مدخل إنساني لا صادم.

**VISUAL DESCRIPTION:** 13A: شاطئ غزة عند الغروب، أمواج هادئة، قوارب صيد خشبية ملوّنة، ظل صيّاد يرمي شبكته من بعيد، مبانٍ خرسانية كثيفة على الساحل في الضباب. 13B: أبو سمير يرتق شبكة خضراء على حافة قارب أزرق وأبيض في الميناء.

**CAMERA ANGLE:** 13A: مستوى العين من الشاطئ. 13B: Medium close-up بمستوى العين.

**CAMERA MOVEMENT:** 13A: Locked-off مع Push-in بطيء نحو البحر. 13B: Handheld خفيف شبه ثابت.

**LENS:** 13A: 35mm. 13B: 50mm.

**LIGHTING:** الساعة الذهبية والغروب — برتقالي-وردي، ظلال زرقاء.

**ENVIRONMENT:** L4 — ساحل غزة وميناء الصيد.

**CHARACTER DESCRIPTION:** أبو سمير (C5).

**CHARACTER CONSISTENCY NOTES:** القميص الكحلي الباهت بأكمام مطوية، شعر رمادي قصير، لحية خفيفة ملحية. الظل البعيد في 13A يمكن أن يكون هو.

> **توصية:** لقطات غزة الحقيقية (من مصوّرين صحفيين ووثائقيين غزّيين بترخيص) هي الخيار الأول أخلاقيًا ومهنيًا. استخدم التوليد فقط للّقطات الرمزية العامة (البحر)، وأفصح عنه.

**IMAGE GENERATION PROMPT — 13A**
<!-- IMG 13A -->
```text
Cinematic documentary photograph, wide shot of the Mediterranean shoreline of Gaza at sunset: calm low waves rolling onto a long sandy beach, a few small brightly painted wooden fishing boats anchored offshore and two pulled up onto the sand, the silhouette of a fisherman standing knee-deep casting a net in the distance, dense concrete city buildings along the coast in soft haze. The sun low over the sea near the horizon, a warm orange-to-rose sky with thin clouds, reflections glittering on the wet sand. Eye level from the beach, 35mm prime lens, horizon on the lower third, boats on the right third, deep focus. Natural, restrained warm grade, not oversaturated, Kodak Vision3 250D emulation, subtle grain, photorealistic, peaceful and quietly melancholic, 16:9, no text, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 13A**
<!-- I2V 13A -->
```text
Locked-off wide shot with a very slow push-in toward the sea. Gentle waves roll in and recede naturally with realistic foam; anchored boats rock slowly; the distant fisherman's net opens and falls; seagulls glide across; sunlight glitters on the water. The horizon stays level and stable, no warping of buildings. 7 seconds.
```

**IMAGE GENERATION PROMPT — 13B**
<!-- IMG 13B -->
```text
Cinematic documentary portrait of a 55-year-old Palestinian fisherman from Gaza sitting on the edge of a small blue-and-white wooden boat at the fishing harbor, mending a green fishing net stretched across his knees, golden hour. Wiry strong build, deeply sun-darkened skin, salt-and-pepper stubble, short grey hair, crow's feet around kind tired eyes, a focused gentle expression; faded navy-blue long-sleeve cotton shirt with rolled sleeves, dark work trousers rolled at the ankles, plastic sandals. Background: other fishing boats, coiled ropes, floats and the harbor wall in soft focus, the sea glowing. Warm low sun from the side, a soft rim on his face and hands. Medium close-up at eye level, 50mm prime lens, shallow depth of field, subject on the left third. Natural skin texture with pores, salt and sun damage, realistic hands, restrained warm grade, subtle grain, photorealistic, dignified, 16:9, no text, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 13B**
<!-- I2V 13B -->
```text
Subtle handheld documentary motion, nearly static. The fisherman's hands work the net with a wooden netting needle in slow, practiced movements, pulling a knot tight; he breathes and blinks naturally and glances once toward the sea; the boat rocks very slightly; water reflections dance on the hull. Hands anatomically correct, net pattern consistent, face identity stable. 6 seconds.
```

**MOTION GRAPHICS:** MG-08 — «غزة» عنوان صغير هادئ في منتصف أسفل الكادر على 13A (02:08–02:11).

**VOICE OVER:** (يبدأ عند 02:09)
> وعلى شاطئِ المتوسّط، تقفُ غزّة...
> ضيّقةً في مساحتِها، واسعةً بأهلِها.
> يخرجُ صيّادوها إلى البحرِ قبلَ الفجر، بحثًا عن رزقِ يومِهم.

**SOUND EFFECTS:** أمواج متوسطية هادئة، نوارس، محرّك قارب صغير بعيد، احتكاك الشبكة والحبال، طقطقة خشب القارب.

**MUSIC:** Cue M5 «غزة» — Strings منخفضة دافئة + لحن Cello هادئ، الأمواج جزء من الموسيقى.

**TRANSITION TO NEXT SCENE:** Cut هادئ من وجه أبو سمير إلى عتبة بيت أم ليلى (الانتقال من البحر إلى البيت).

**NEGATIVE PROMPT:** NEG-IMAGE + `luxury yachts, resort beach, tourists in swimwear, sunbathers, warships, explosions, smoke columns, tropical palm resort, turquoise Caribbean water`

---

### المشهد 14 — غزة والإنسان
**الفصل الخامس**

**SCENE NUMBER:** 14

**TIME CODE:** 02:19 – 02:33

**DURATION:** 14 ثانية (14A: 4 ث — 14B: 3.5 ث — 14C: 3 ث — 14D: 3.5 ث)

**PURPOSE OF THE SCENE:** وجوه غزة كبشر لا كأرقام: أمّ وأطفال، شاب، مسنّ، بائع. الاعتراف بالحصار والحروب والنزوح دون صور صادمة — الحياة تحاول أن تبدأ من جديد.

**VISUAL DESCRIPTION:** 14A: أم ليلى على عتبة بيت خرساني بسيط تجدل شعر ليلى، وأخوها الصغير يتّكئ على كتفها بسيارة لعبة؛ في الخلفية البعيدة ضبابيًا مبانٍ متضررة (سياق صادق غير صادم). 14B: شاب يمشي في شارع مزدحم بغزة يحمل كتبًا وكيس خبز. 14C: رجل مسنّ يجلس أمام دكان بمسبحة. 14D: بائع خضار يرتّب البندورة والنعناع.

**CAMERA ANGLE:** 14A: جالس بمستوى العين. 14B: ¾ أمامي منخفض قليلًا. 14C: Medium close-up. 14D: متوسطة.

**CAMERA MOVEMENT:** Handheld documentary خفيف في الجميع؛ 14B Tracking للخلف.

**LENS:** 14A: 50mm. 14B: 35mm. 14C: 85mm. 14D: 35mm.

**LIGHTING:** آخر العصر ← غسق؛ ضوء دافئ منخفض، غبار في الهواء.

**ENVIRONMENT:** L4 — شوارع رملية، جدران خرسانية غير مكسوّة، أسلاك كهرباء متشابكة، دكاكين صغيرة.

**CHARACTER DESCRIPTION:** أم ليلى (C7)، ليلى (C6)، أخوها (5 أعوام)، شاب (~22)، مسنّ (~78)، بائع (~45).

**CHARACTER CONSISTENCY NOTES:** **ليلى:** الكارديغان الأصفر الخردلي + الضفيرة الطويلة — ستظهر بنفس الملابس في 15A. منديل الأم وردي مغبرّ.

> **توصية:** كما في م13 — اللقطات الحقيقية المرخّصة أولًا. لا تستخدم أبدًا صورًا مولّدة لأطفال غزة في سياق يوحي بأنها توثيق لحدث حقيقي.

**IMAGE GENERATION PROMPT — 14A**
<!-- IMG 14A -->
```text
Cinematic documentary photograph of a 36-year-old Palestinian mother in Gaza sitting on the doorstep of a modest concrete home with her two children in the late afternoon. She wears a dusty-rose headscarf and a long dark-grey coat-dress, has warm tired eyes and a soft genuine smile, and is braiding the hair of her 9-year-old daughter, who has a long dark-brown braid, olive skin and thoughtful dark eyes and wears a mustard-yellow knitted cardigan over a white t-shirt; a 5-year-old boy leans on his mother's shoulder holding a small toy car. A narrow sandy street, unplastered concrete walls, a potted plant, a water jerrycan; some distant damaged buildings softly blurred far in the background. Warm low sunlight from the right, soft shadows. Medium shot at seated eye level, 50mm prime lens, shallow depth of field, the family center-left. Natural, tender, unposed, realistic faces, natural skin texture, restrained warm grade, subtle grain, photorealistic, non-graphic, 16:9, no text, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 14A**
<!-- I2V 14A -->
```text
Static camera with subtle handheld breathing. The mother's fingers continue braiding her daughter's hair with natural, careful motion; the daughter blinks and smiles slightly; the little boy shifts his weight and rolls the toy car along his mother's arm. Natural breathing, consistent faces, correct hands, no morphing. 6 seconds.
```

**IMAGE GENERATION PROMPT — 14B**
<!-- IMG 14B -->
```text
Cinematic documentary photograph of a Palestinian young man in his early twenties walking along a busy street in Gaza City in the late afternoon, carrying a stack of books under one arm and a small bag of bread in the other hand, seen from a slightly low three-quarter front angle. Short black hair, light beard, a focused calm expression; grey hoodie, dark jeans, worn sneakers. Around him: street vendors, a few cars and motorbikes, small shopfronts with blurred unreadable signs, concrete buildings with balconies, overhead tangles of electric wires. Warm hazy light with dust in the air. 35mm lens, moderate depth of field, the young man sharp and the background softly blurred. Authentic everyday street life, restrained grade, subtle grain, photorealistic, 16:9, no readable text, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 14B**
<!-- I2V 14B -->
```text
Slow backward tracking shot at walking pace with natural handheld sway. The young man walks with a natural gait and glances to the side at a passing motorbike; background people move naturally; dust drifts in the light. Feet grounded, no sliding, consistent face, the books keep their shape. 5 seconds.
```

**IMAGE GENERATION PROMPT — 14C**
<!-- IMG 14C -->
```text
Cinematic documentary portrait of an elderly Palestinian man in his late seventies in Gaza, sitting on a plastic chair in front of a small shop at dusk, holding a string of prayer beads and looking calmly at the street. White stubble, a deeply lined face, kind patient eyes, a white knitted skullcap, a light-brown jacket over a white shirt. The last warm light on his face, soft shadows. Medium close-up, 85mm lens, shallow depth of field, background street lights and passing figures in soft bokeh. Natural skin texture, quiet dignity, restrained warm grade, subtle grain, photorealistic, 16:9, no text, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 14C**
<!-- I2V 14C -->
```text
Extremely slow push-in. The man passes the beads slowly between his fingers, breathes, blinks, and gives a small gentle nod to someone off-camera. Face and hands stable, no morphing. 5 seconds.
```

**IMAGE GENERATION PROMPT — 14D**
<!-- IMG 14D -->
```text
Cinematic documentary photograph of a Palestinian vegetable vendor in his forties at a market stall in Gaza in the late afternoon, arranging tomatoes, cucumbers, eggplants and bunches of fresh mint and parsley on a wooden cart under a faded canvas shade; short dark hair, trimmed beard, a cheerful focused face; dark-green jacket over a t-shirt. A woman customer in a headscarf chooses produce in the slightly out-of-focus foreground. Warm side light filtering through the canvas, rich but natural colors. Medium shot, 35mm lens, moderate depth of field. Authentic everyday market, natural skin texture, restrained grade, subtle grain, photorealistic, 16:9, no readable text, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 14D**
<!-- I2V 14D -->
```text
Subtle handheld motion. The vendor places a tomato on the pile and hands a small bunch of mint to the customer with a smile; the canvas shade moves slightly in the breeze; natural crowd movement in the background. Correct hands, consistent produce, no morphing. 5 seconds.
```

**MOTION GRAPHICS:** MG-02 (اختياري) — «الإنسان» صغيرة على 14C.

**VOICE OVER:** (يبدأ عند 02:20)
> عرفَت غزّةُ الحصارَ والحروبَ والنزوح...
> لكنّ الحياةَ فيها تحاولُ كلَّ صباحٍ أن تبدأَ من جديد:
> أمٌّ تجدلُ شَعرَ ابنتِها، وشابٌّ يحملُ كتبَه، وبائعٌ يرتّبُ بضاعتَه.

**SOUND EFFECTS:** أصوات حيّ (أطفال، باب حديدي، دراجة نارية بعيدة)، سوق بالعربية بلهجة غزّية، حبّات مسبحة، أكياس ورقية، ريح بحرية خفيفة. **لا** طائرات ولا انفجارات.

**MUSIC:** M5 يستمر، ويبدأ التحوّل اللوني الموسيقي نحو الأمل في آخر 3 ثوانٍ (من الحجاز إلى الراست).

**TRANSITION TO NEXT SCENE:** Cut على الشخصية: من ليلى على العتبة (14A) — تُعاد لحظيًا — إلى ليلى على الشاطئ (15A). أو Cross-dissolve على ضوء الغروب.

**NEGATIVE PROMPT:** NEG-IMAGE + `blood, injuries, bandages close-up, dead bodies, crying children close-up, explosions, smoke columns, aircraft, rubble as main subject, refugee stereotypes, begging gestures, pity framing, looking at camera pleading`

---

### المشهد 15 — الأمل
**الفصل السادس: الهوية والأمل والمستقبل**

**SCENE NUMBER:** 15

**TIME CODE:** 02:33 – 02:43

**DURATION:** 10 ثوانٍ (لقطة واحدة)

**PURPOSE OF THE SCENE:** الجملة الأهم إنسانيًا في الفيلم. التحوّل من "خبر" إلى "إنسان". ذروة الأمل الهادئ.

**VISUAL DESCRIPTION:** ليلى واقفة حافية على الرمل المبلل عند الغروب، تُرى جانبيًا من الخلف قليلًا، تنظر نحو الأفق. ضوء ذهبي يحيط بشعرها وكارديغانها. قوارب بعيدة.

**CAMERA ANGLE:** مستوى عين الطفلة، بروفايل ¾ من الخلف.

**CAMERA MOVEMENT:** Push-in بطيء جدًا مع Arc خفيف نحو وجهها.

**LENS:** 85mm.

**LIGHTING:** شمس منخفضة عند الأفق، Rim light ذهبي، دفء هادئ.

**ENVIRONMENT:** L4 — شاطئ غزة (استمرار 13A).

**CHARACTER DESCRIPTION:** ليلى (C6).

**CHARACTER CONSISTENCY NOTES:** نفس الكارديغان الخردلي والضفيرة من 14A. وجهها هادئ مع بداية ابتسامة — لا حزن ولا "ابتسامة إعلانية".

**IMAGE GENERATION PROMPT — 15A**
<!-- IMG 15A -->
```text
Cinematic documentary photograph of a 9-year-old Palestinian girl from Gaza standing barefoot on the wet sand of the beach at sunset, seen in profile from slightly behind, looking toward the horizon over the sea. Slender, olive skin, dark-brown hair in a single long braid, thoughtful dark eyes, a calm expression with the faint beginning of a smile; a mustard-yellow knitted cardigan over a white t-shirt and dark-blue trousers. The warm low sun near the horizon creates a soft golden rim light around her hair and cardigan; gentle waves and a few distant fishing boats behind. Medium shot at her eye level, 85mm prime lens, very shallow depth of field, the girl on the left third with open space toward the sea, sea and sky in soft bokeh. Natural skin texture, restrained warm golden grade, not oversaturated, Kodak Vision3 250D emulation, subtle grain, photorealistic, hopeful and quiet, 16:9, no text, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 15A**
<!-- I2V 15A -->
```text
Very slow push-in with a slight arc toward her face. The sea breeze moves stray hairs and the edge of the cardigan; she breathes calmly, blinks, and slowly lifts her chin a little toward the horizon; waves glisten in the background bokeh. Face identity stable, braid consistent, no facial distortion. 7 seconds.
```

**MOTION GRAPHICS:** MG-02 (اختياري) — «الأمل» صغيرة أسفل يمين الكادر في آخر ثانيتين.

**VOICE OVER:** (يبدأ عند 02:34)
> خلفَ الأخبارِ والأرقام، هناك إنسان...
> له اسم، وبيت، وذكريات... وأحلام.

**SOUND EFFECTS:** أمواج ناعمة أقرب، ريح بحرية في الشعر (Foley ناعم)، نورس واحد بعيد.

**MUSIC:** Cue M6 «الأمل» يبدأ — الوتريات تتّسع، لحن العود يعود بلون مقام الراست (أكثر إشراقًا).

**TRANSITION TO NEXT SCENE:** Cross-dissolve على وهج الشمس: من شمس البحر إلى وهج الشمس بين أغصان الزيتونة العتيقة.

**NEGATIVE PROMPT:** NEG-IMAGE + `posed model, fashion editorial, glamour, makeup, staring into camera, sad crying face, oversaturated sunset, sun flare covering face, different clothing than reference`

---

### المشهد 16 — شجرة الزيتون
**الفصل السادس**

**SCENE NUMBER:** 16

**TIME CODE:** 02:43 – 02:53

**DURATION:** 10 ثوانٍ (لقطة واحدة)

**PURPOSE OF THE SCENE:** الاستعارة الجامعة: الجذور والاستمرار. براعم جديدة تنبت من قاعدة جذع عتيق — الغصن الجديد من الجذر القديم.

**VISUAL DESCRIPTION:** زيتونة قديمة جدًا على مدرّج حجري عند الساعة الذهبية: جذور ضخمة تقبض على التربة الحمراء والحجر، جذع ملتوٍ متعدد السيقان، **براعم خضراء فتية** تنبت من القاعدة، والكاميرا تصعد من الجذور إلى التاج المضيء والسماء.

**CAMERA ANGLE:** زاوية منخفضة جدًا من مستوى الجذور.

**CAMERA MOVEMENT:** Crane/tilt-up مستمر بطيء من الجذور إلى السماء.

**LENS:** 24mm (الاستثناء الوحيد في الفيلم).

**LIGHTING:** ساعة ذهبية، إضاءة خلفية للأوراق، وهج شمس ناعم.

**ENVIRONMENT:** L1 — مدرّجات زيتون.

**CHARACTER DESCRIPTION:** لا شخصيات.

**CHARACTER CONSISTENCY NOTES:** نفس نوع الجذع وملمس اللحاء كما في 2B (يُستحسن أن تبدو الشجرة نفسها — دائرة بصرية).

**IMAGE GENERATION PROMPT — 16A**
<!-- IMG 16A -->
```text
Cinematic documentary photograph of a very ancient Palestinian olive tree on a stone terrace at golden hour, framed from ground level at its base: enormous gnarled roots gripping red soil and limestone rocks, a massive twisted multi-stemmed trunk rising upward, young green shoots sprouting from the old base; a silver-green canopy above glowing in warm backlight against a clear sky turning amber. Terraced hills with more olive trees in the background. Extreme low angle, 24mm prime lens, deep focus, strong vertical composition. Rich bark and soil texture, warm restrained grade, gentle sun flare, Kodak Vision3 250D emulation, subtle grain, photorealistic, timeless and resilient, no people, 16:9, no text, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 16A**
<!-- I2V 16A -->
```text
Slow continuous vertical crane and tilt-up starting at the roots and young shoots, rising along the twisted trunk to the glowing canopy and the open sky, ending on soft sun flare through the leaves. Leaves move in a light breeze, light rays flicker naturally. The trunk geometry stays stable, no morphing bark. 8 seconds.
```
> خطة بديلة: ولّد نسخة **طولية 9:16** من الصورة نفسها، واصنع حركة الصعود بـ Pan عمودي داخل المونتاج.

**MOTION GRAPHICS:** لا شيء.

**VOICE OVER:** (يبدأ عند 02:44)
> هكذا هي الحكاية... كشجرةِ زيتونٍ عتيقة:
> جذورُها ضاربةٌ في الأرض،
> وكلّما قُطِعَ منها غصن، أنبتَت غصنًا جديدًا.

**SOUND EFFECTS:** حفيف أوراق الزيتون في ريح المساء (أساسي)، طيور الغروب، صرصار خافت.

**MUSIC:** M6 يتصاعد — Soft percussion يدخل، الوتريات تبني نحو الذروة.

**TRANSITION TO NEXT SCENE:** **Light film transition:** وهج الشمس يغمر الكادر (White bloom 8 فريمات) ← يبدأ المونتاج الختامي على الإيقاع.

**NEGATIVE PROMPT:** NEG-IMAGE + `fantasy tree, glowing magical light, tree of life illustration, giant oak, baobab, people, swing, dead tree`

---

### المشهد 17 — مونتاج الخاتمة
**الفصل السادس**

**SCENE NUMBER:** 17

**TIME CODE:** 02:53 – 03:02

**DURATION:** 9 ثوانٍ

**PURPOSE OF THE SCENE:** الذروة العاطفية: تكثيف الفيلم كله في نبضات. ينتهي بتسليم المفتاح من الجدّ إلى الحفيد — الذاكرة تُورَّث.

**VISUAL DESCRIPTION — تسلسل المونتاج (قطعات على إيقاع الموسيقى، كل لقطة بسرعة 80% بـ Optical flow إن لزم):**
| # | اللقطة | المصدر | المدة |
|---|---|---|---|
| 1 | الأرض — التراب في اليد | 02A | 0.9 ث |
| 2 | الزيتون — الجذع | 02B | 0.9 ث |
| 3 | الأطفال — الزقاق | 03C | 0.9 ث |
| 4 | البحر — غروب غزة | 13A | 1.0 ث |
| 5 | العائلة — الأم وليلى | 14A | 1.0 ث |
| 6 | المدينة — الأسطح | 12C | 0.9 ث |
| 7 | البيت — القوس والصبّار | 09B | 0.9 ث |
| 8 | **المفتاح — التسليم** | **17A (جديدة)** | **2.5 ث** |

**CAMERA ANGLE:** 17A: جانبية بمستوى اليدين.

**CAMERA MOVEMENT:** 17A: Locked-off مع Push-in بطيء جدًا.

**LENS:** 17A: 85mm.

**LIGHTING:** 17A: ساعة ذهبية، إضاءة خلفية من كرم الزيتون.

**ENVIRONMENT:** 17A: L1 — كرم زيتون.

**CHARACTER DESCRIPTION:** يد أبو خليل (C1) + يد يوسف (C3).

**CHARACTER CONSISTENCY NOTES:** الخاتم الفضي + الكمّ الرمادي (الجدّ)؛ كمّ القميص الأزرق الفاتح (الحفيد)؛ **المفتاح مطابق تمامًا** لـ 8A/8B (استخدم المرجع).

**IMAGE GENERATION PROMPT — 17A**
<!-- IMG 17A -->
```text
Cinematic documentary close-up of two hands at golden hour: the deeply lined, weathered hand of an 86-year-old Palestinian man, with a plain thin silver ring on the right ring finger and a charcoal-grey wool jacket cuff, gently placing an old hand-forged iron key with a large oval bow, long shaft and dark patina into the open small palm of a 10-year-old boy whose light-blue shirt cuff is visible. Background: an olive grove in warm backlight, soft bokeh. Side angle at hand level, 85mm lens, very shallow depth of field, the key in sharp focus centered between the hands. Natural skin textures, a clear contrast of old and young skin, warm restrained grade, Kodak Vision3 250D emulation, subtle grain, photorealistic, tender and solemn, 16:9, no text, no watermark.
```

**IMAGE-TO-VIDEO PROMPT — 17A**
<!-- I2V 17A -->
```text
Locked-off shot with a very slow push-in. The old hand lowers the key slowly into the boy's palm and lingers for a moment; the boy's fingers close gently around the key; leaves shimmer in the background bokeh. Exactly two hands, five fingers each, the key's shape identical to the reference, no morphing. 6 seconds.
```

**MOTION GRAPHICS:** لا شيء.

**VOICE OVER:** (يبدأ عند 02:54)
> فلسطينُ ليست خطًّا على خريطة...
> إنّها قصّةُ شعب، وذاكرةُ بيت، وإنسانٌ لم يتوقّف عن الحلم.

**SOUND EFFECTS:** طبقات خفيفة متقاطعة على كل قطعة (تراب، أوراق، ضحكة طفل، موجة، رنين مفتاح) — منخفضة جدًا، الموسيقى هي القائد هنا. رنين المفتاح الأخير أوضح قليلًا.

**MUSIC:** **ذروة M6** عند 02:58 تقريبًا (وتريات كاملة + عود + إيقاع ناعم)، ثم تنسحب الطبقات واحدة تلو الأخرى مع لقطة المفتاح.

**TRANSITION TO NEXT SCENE:** Slow fade to black (24 فريم) على يد يوسف المنغلقة على المفتاح.

**NEGATIVE PROMPT:** NEG-IMAGE + `three hands, extra hands, different key shape, modern key, gloves, jewelry on child, fast flashy montage effects, glitch transitions`

---

### المشهد 18 — العنوان الختامي
**الفصل السادس**

**SCENE NUMBER:** 18

**TIME CODE:** 03:02 – 03:10

**DURATION:** 8 ثوانٍ

**PURPOSE OF THE SCENE:** الإغلاق: صمت، كلمة واحدة، هوية.

**VISUAL DESCRIPTION:** شاشة داكنة (Charcoal) بملمس ورقي خفيف جدًا. تظهر «فلسطين» ببطء، ثم تحتها «الأرض • الذاكرة • الإنسان».

**CAMERA ANGLE:** —

**CAMERA MOVEMENT:** Push-in افتراضي بالغ البطء (100% ← 103%).

**LENS:** —

**LIGHTING:** توهّج خفيف جدًا خلف الكلمة (Glow 5%).

**ENVIRONMENT:** —

**CHARACTER DESCRIPTION:** —

**CHARACTER CONSISTENCY NOTES:** —

**IMAGE GENERATION PROMPT:** لا يوجد (Motion Graphics). خلفية الورق الداكن: انظر MG-09 في `05_MOTION_GRAPHICS.md`.

**IMAGE-TO-VIDEO PROMPT:** لا يوجد.

**MOTION GRAPHICS:** MG-09:
- 03:02 أسود + صمت.
- 03:03 ينطق الراوي الجملة الأخيرة.
- 03:04.5 تظهر «فلسطين» مع نطق الكلمة (Fade 24 فريم + انجراف 8px للأعلى) — Amiri، Off-White.
- 03:06.5 يظهر السطر الثاني «الأرض • الذاكرة • الإنسان» (IBM Plex Sans Arabic Light) — الفاصلتان «•» بلون Tatreez Red المكتوم.
- 03:09 Fade out كامل إلى أسود.

**VOICE OVER:** (يبدأ عند 03:03، بعد ثانية صمت كاملة)
> ولهذه الحكايةِ... اسمٌ واحد:
> فلسطين.

**SOUND EFFECTS:** لا شيء. صمت تام قبل الجملة. بعد كلمة «فلسطين»: نَفَس ريح واحد خافت جدًا وحفيف ورقة زيتون.

**MUSIC:** Cue M7 «الخاتمة» — نغمة عود واحدة أخيرة تُعزف **بعد** كلمة «فلسطين» مباشرة، مع ذيل صدى 4 ثوانٍ يتلاشى إلى صمت.

**TRANSITION TO NEXT SCENE:** Fade to black ← (اختياري) شارة الاعتمادات والشفافية MG-10 لمدة 8 ثوانٍ.

**NEGATIVE PROMPT:** لا ينطبق.

---

## سادسًا: الجدول المختصر

| # | المدة | نوع اللقطة | نوع الصورة | حركة الكاميرا | التعليق الصوتي (البداية) | الموسيقى | المؤثرات الصوتية | الانتقال |
|---|---|---|---|---|---|---|---|---|
| 01 | 13ث | Extreme wide | AI | Slow push-in | «هناكَ أماكنُ لا تُختصَر...» | M1 Drone | ريح فجر، ديك، طيور | Cross-dissolve |
| 02 | 11ث | Macro + Low wide | AI | Push-in / Tilt-up | «هنا، لم تكنِ الأرضُ...» | M1 + أول نغمات عود | تراب، أوراق زيتون | Match on light |
| 03 | 11ث | Medium ×3 | AI | Handheld / Dolly | «في القرى، يخرجُ الخبزُ...» | M2 عود + دف خفيف | طابون، معول، أطفال | Color drain ← أرشيف |
| 04 | 10ث | Stills | **أرشيف حقيقي** | Ken Burns | «وفي المدن، كان برتقالُ يافا...» | M2 | ميناء، سوق خافت | Dissolve إلى الخريطة |
| 05 | 8ث | Map | **Motion Graphics** | Virtual push-in | «كانت حياةً عاديّة...» | M2 ← توقف مفاجئ | قلم، نقرات، صمت | Hard cut بعد صمت |
| 06 | 16ث | Stills/Film | **أرشيف حقيقي** | Ken Burns بطيء | «في خضمِّ حربِ ذلك العام...» | M3 Cello حجاز | ريح باردة، صمت | Slow fade |
| 07 | 9ث | Ground + Extreme wide | AI (تمثيلي مُعلَن) | Follow / Push-in | «حملوا ما استطاعوا...» | M3 + Strings | خطوات، قماش، ريح | Fade to black قصير |
| 08 | 12ث | Macro + MCU | AI | Orbit / Push-in | «ولذلك، احتفظَ كثيرون...» | M3b عود منفرد | رنين مفتاح، ساعة | Match cut على اليد |
| 09 | 9ث | CU + Medium wide | AI | Static / Dolly | «صورٌ قديمة...» | M3 يتلاشى | صفحات، ريح عشب | J-cut جرس مدرسة |
| 10 | 9ث | Medium wide ×2 | AI | Tracking / Handheld | «واليوم، يحملُ جيلٌ جديد...» | M4 نبض يعود | جرس، صف | Cross-dissolve |
| 11 | 9ث | Medium wide + Macro | AI | Pedestal down / Push-in | «وفي كلِّ خريف...» | M4 يتصاعد | زيتون على الشادر | Beat cut |
| 12 | 10ث | Medium ×2 + Wide | AI (يُفضَّل حقيقي) | Handheld / Slide / Pan | «وفي المدن، تمضي الحياةُ...» | M4 يهدأ | سوق، مقهى، حمام | Match on light |
| 13 | 12ث | Wide + MCU | AI (يُفضَّل حقيقي) | Push-in / Handheld | «وعلى شاطئِ المتوسّط...» | M5 Strings + Cello | أمواج، نوارس، شباك | Cut إلى البيت |
| 14 | 14ث | Medium ×4 | AI (يُفضَّل حقيقي) | Handheld / Tracking | «عرفَت غزّةُ الحصارَ...» | M5 ← تحوّل للأمل | حيّ، سوق، مسبحة | Cut على الشخصية |
| 15 | 10ث | Medium (85mm) | AI | Push-in + arc | «خلفَ الأخبارِ والأرقام...» | M6 راست | أمواج، ريح | Dissolve على الوهج |
| 16 | 10ث | Low angle (24mm) | AI | Crane/Tilt-up | «هكذا هي الحكاية...» | M6 يبني | أوراق زيتون | White bloom |
| 17 | 9ث | Montage + CU | AI (إعادة استخدام + 17A) | Cuts على الإيقاع | «فلسطينُ ليست خطًّا...» | **ذروة M6** | طبقات خفيفة، مفتاح | Fade to black |
| 18 | 8ث | Title card | **Motion Graphics** | Virtual push-in | «ولهذه الحكايةِ... فلسطين.» | M7 نغمة عود أخيرة | صمت ثم نَفَس ريح | Fade out |
| **∑** | **3:10** | | | | | | | |

**إحصاء اللقطات:** 28 صورة مولّدة (لقطات AI) + 6–8 صور أرشيفية + 4 لوحات Motion Graphics رئيسية.

---

## سابعًا: المخرجات النهائية

| # | المطلوب | الملف |
|---|---|---|
| 1 | النص الكامل للتعليق الصوتي + الترجمة الإنجليزية + توجيهات الأداء | [`02_VOICEOVER.md`](02_VOICEOVER.md) + `subtitles/` |
| 2 | جميع Prompts الصور مرتبة | [`03_IMAGE_PROMPTS.md`](03_IMAGE_PROMPTS.md) |
| 3 | جميع Prompts تحريك الصور مرتبة | [`04_VIDEO_PROMPTS.md`](04_VIDEO_PROMPTS.md) |
| 4 | Prompts ومواصفات Motion Graphics | [`05_MOTION_GRAPHICS.md`](05_MOTION_GRAPHICS.md) |
| 5 | الموسيقى والمؤثرات الصوتية | [`06_MUSIC_AND_SFX.md`](06_MUSIC_AND_SFX.md) |
| 6 | تعليمات المونتاج النهائية | [`07_EDIT_GUIDE.md`](07_EDIT_GUIDE.md) |
| 7 | المصادر وجدول التحقق من الحقائق | [`08_SOURCES.md`](08_SOURCES.md) |

---

## ثامنًا: سياسة الشفافية والأخلاقيات

1. **التاريخ = أرشيف حقيقي.** لا صور تاريخية مولّدة، لا تلوين، لا تحريك AI لصور أشخاص حقيقيين.
2. **المولَّد = تمثيلي ومُعلَن.** وسم «مشهد تمثيلي» على م7، وسطر في الشارة الختامية: «بعض المشاهد في هذا الفيلم مشاهد تمثيلية أُنتجت بمساعدة الذكاء الاصطناعي؛ جميع الصور التاريخية أرشيفية وموثّقة المصدر.»
3. **غزة:** الأولوية للقطات حقيقية مرخّصة من مصوّرين فلسطينيين، مع ذكر أسمائهم.
4. **الأرقام:** لا رقم على الشاشة أو في التعليق إلا وله مصدر في `08_SOURCES.md`.
5. **الكرامة:** لا دماء، لا جثث، لا أطفال يبكون للاستدرار، لا تأطير "شفقة"، لا صور نمطية.
6. **لا أسماء حقيقية لشخصيات تمثيلية**، ولا نسب قصص مختلقة إلى أشخاص في صور أرشيفية.
