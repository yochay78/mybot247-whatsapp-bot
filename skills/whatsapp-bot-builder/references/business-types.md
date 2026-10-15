# Business types and their questions

Each bot starts from one of these types. Question ids are the only ids the link may refer to.
`ON` questions are asked by default, `OFF` ones are offered to the owner as optional. The `name` question (asking the customer's name) always stays on.

## `solo2_ac` - טכנאי מזגנים (air-conditioning technician)
- `problem` ON: מה הבעיה במזגן? [options: לא מקרר, נוזל מים, רעש, התקנה חדשה]
- `city` ON: באיזו עיר?
- `urgency` ON: כמה זה דחוף? [options: היום, השבוע, לא דחוף]
- `photo` OFF: אפשר לשלוח כאן תמונה של מה שצריך, ואחריה לכתוב "שלחתי". אם אין תמונה, כתבו "דלג"
- `name` ON: איך קוראים לך?

## `solo2_beauty` - יופי וטיפוח (beauty and personal care)
- `treatment` ON: איזה טיפול מעניין אותך?
- `times` ON: באילו ימים או שעות הכי נוח לך?
- `event` OFF: זה לקראת אירוע מסוים? [options: כן, סתם בשביל עצמי]
- `photo` OFF: יש תמונה של סגנון שאהבת? אפשר לשלוח כאן ואחריה לכתוב "שלחתי". אם אין, כתבו "דלג"
- `first_time` OFF: זו הפעם הראשונה שלך אצלנו? [options: כן, כבר הייתי]
- `name` ON: איך קוראים לך?

## `solo2_car` - שירותי רכב (car services)
- `service` ON: איזה שירות לרכב צריך?
- `car` ON: מה סוג הרכב?
- `area` ON: באיזה אזור?
- `times` OFF: מתי נוח לך?
- `photo` OFF: יש תמונה שיכולה לעזור? אפשר לשלוח כאן ואחריה לכתוב "שלחתי". אם אין, כתבו "דלג"
- `name` ON: איך קוראים לך?

## `solo2_catering` - קייטרינג ועוגות (catering and cakes)
- `event` ON: לאיזה אירוע?
- `date` ON: לאיזה תאריך?
- `people` ON: לכמה אנשים בערך? [options: עד 10, 10 עד 30, מעל 30]
- `city` OFF: מאיזו עיר? (בשביל המשלוח)
- `allergies` OFF: יש רגישויות שחשוב שנדע?
- `name` ON: איך קוראים לך?

## `solo2_cleaning` - ניקיון בתים ומשרדים (home and office cleaning)
- `kind` ON: איזה ניקיון צריך? [options: בית, משרד, לפני או אחרי מעבר, אחר]
- `city` ON: באיזו עיר?
- `size` ON: כמה חדרים, או מה גודל המקום בערך?
- `when` OFF: מתי צריך את הניקיון?
- `name` ON: איך קוראים לך?

## `solo2_clinic` - טיפול וקליניקה (therapy and clinic)
- `service` ON: איזה סוג טיפול או ייעוץ מעניין אותך?
- `for_whom` ON: הטיפול בשבילך או בשביל מישהו אחר? [options: בשבילי, בשביל הילד או הילדה, בשביל מישהו אחר]
- `times` ON: מתי בדרך כלל נוח לך להגיע?
- `where` OFF: מעדיפים קליניקה או אונליין? [options: קליניקה, אונליין, לא משנה]
- `before` OFF: היית אצלנו בעבר? [options: כן, לא]
- `name` ON: איך קוראים לך?

## `solo2_driving` - מורי נהיגה (driving instructor)
- `license` ON: איזה שיעורי נהיגה מחפשים? [options: רכב אוטומט, רכב ידני, אופנוע, משהו אחר]
- `area` ON: מאיזו עיר או שכונה נוח להתחיל?
- `theory` ON: כבר עברת תאוריה? [options: כן, עדיין לא]
- `times` OFF: מתי בדרך כלל נוח לך ללמוד?
- `for_whom` OFF: השיעורים בשבילך או בשביל הבן או הבת? [options: בשבילי, בשביל הבן או הבת]
- `name` ON: איך קוראים לך?

## `solo2_garden` - גינון (gardening)
- `work` ON: איזו עבודה צריך? [options: תחזוקה קבועה, עבודה חד פעמית, תכנון גינה]
- `city` ON: באיזו עיר?
- `size` ON: מה גודל הגינה בערך?
- `often` OFF: כל כמה זמן? (לתחזוקה)
- `name` ON: איך קוראים לך?

## `solo2_general` - עסק אחר (any other business)
Also needs `field`: what the business does, up to 40 characters.
- `need` ON: במה אפשר לעזור?
- `urgency` ON: כמה זה דחוף? [options: היום, בימים הקרובים, לא דחוף]
- `times` ON: מתי נוח שנחזור אליך?
- `area` OFF: באיזה אזור צריך את השירות?
- `name` ON: איך קוראים לך?

## `solo2_home` - תיקונים ושיפוצים (home repairs and renovations)
- `need` ON: מה צריך לתקן או לעשות?
- `city` ON: באיזו עיר העבודה?
- `urgency` ON: כמה זה דחוף? [options: ממש דחוף, היום או מחר, השבוע, לא דחוף]
- `photo` ON: אפשר לשלוח כאן תמונה של מה שצריך, ואחריה לכתוב "שלחתי". אם אין תמונה, כתבו "דלג"
- `times` OFF: מתי נוח שנחזור אליך?
- `name` ON: איך קוראים לך?

## `solo2_law` - עורכי דין וייעוץ (lawyers and consulting)
- `topic` ON: באיזה נושא הפנייה? [options: משפחה, מקרקעין, עבודה, אחר]
- `times` ON: מתי נוח שנחזור אליך?
- `deadline` OFF: יש תאריך חשוב שמתקרב?
- `meeting` OFF: מעדיפים פגישה או שיחת טלפון? [options: פגישה, טלפון]
- `name` ON: איך קוראים לך?

## `solo2_moving` - הובלות (moving)
- `what` ON: מה מובילים? [options: דירה, כמה פריטים, משרד]
- `route` ON: מאיפה ולאן?
- `date` ON: לאיזה תאריך?
- `stairs` OFF: יש קומות בלי מעלית? [options: כן, לא]
- `name` ON: איך קוראים לך?

## `solo2_music` - מורים למוזיקה (music teacher)
- `instrument` ON: איזה כלי נגינה מעניין אותך?
- `age` ON: השיעורים לילד או למבוגר? [options: ילד, מבוגר]
- `experience` ON: יש כבר ניסיון? [options: מתחיל/ה, קצת, מנגן/ת]
- `times` OFF: מתי נוח לך לשיעורים?
- `name` ON: איך קוראים לך?

## `solo2_pest` - הדברה (pest control)
- `pest` ON: מה המזיק?
- `city` ON: באיזו עיר?
- `property` ON: איזה נכס? [options: דירה, בית פרטי, עסק]
- `urgency` OFF: כמה זה דחוף? [options: היום, השבוע, לא דחוף]
- `name` ON: איך קוראים לך?

## `solo2_pets` - טיפוח חיות מחמד (pet grooming)
- `treatment` ON: איזה טיפול צריך?
- `pet` ON: איזו חיה, ובאיזה גודל בערך?
- `times` ON: מתי נוח לך?
- `first_time` OFF: פעם ראשונה אצלנו? [options: כן, כבר הייתי]
- `name` ON: איך קוראים לך?

## `solo2_photo` - צילום ואירועים (photography and events)
- `kind` ON: איזה צילום מחפשים? [options: חתונה או אירוע, משפחה או ילדים, תדמית או עסק, משהו אחר]
- `date` ON: יש כבר תאריך? אם כן, כתבו אותו
- `place` ON: איפה הצילום?
- `hours` OFF: כמה שעות צילום בערך?
- `guests` OFF: כמה אורחים בערך? [options: עד 50, 50 עד 200, מעל 200]
- `name` ON: איך קוראים לך?

## `solo2_trainer` - מאמני כושר (personal trainer)
- `goal` ON: מה הכי חשוב לך להשיג? [options: לרדת במשקל, להתחזק, לחזור לכושר, כושר כללי]
- `kind` ON: איזה אימון מעניין אותך? [options: אישי, זוגי, קבוצה קטנה, עוד לא החלטתי]
- `times` ON: מתי הכי נוח לך להתאמן?
- `per_week` OFF: כמה פעמים בשבוע היית רוצה? [options: פעם אחת, פעמיים, שלוש או יותר]
- `notes` OFF: יש משהו שחשוב שהמאמן ידע לפני שמתחילים?
- `name` ON: איך קוראים לך?

## `solo2_tutor` - מורים פרטיים (private tutor)
- `subject` ON: באיזה מקצוע צריך עזרה?
- `grade` ON: לאיזו כיתה או גיל?
- `times` ON: מתי נוח לכם ללמוד?
- `format` OFF: איך מעדיפים ללמוד? [options: פנים אל פנים, אונליין, לא משנה]
- `exam` OFF: יש מבחן או בגרות שמתקרבים? [options: כן, לא, למידה שוטפת]
- `name` ON: איך קוראים לך?

## `solo2_yoga` - יוגה ופילאטיס (yoga and pilates)
- `lesson` ON: איזה שיעור מעניין אותך? [options: יוגה, פילאטיס, שניהם, אשמח להכוונה]
- `experience` ON: יש לך כבר ניסיון? [options: מתחיל/ה לגמרי, קצת ניסיון, מתרגל/ת קבוע]
- `times` ON: מתי נוח לך להגיע?
- `format` OFF: מה מתאים לך? [options: קבוצה, שיעור פרטי, אונליין]
- `notes` OFF: יש משהו שחשוב שנדע מראש?
- `name` ON: איך קוראים לך?
